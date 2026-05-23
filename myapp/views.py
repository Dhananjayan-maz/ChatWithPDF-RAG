from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
from django.contrib.auth import authenticate, login

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI


def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # Do not save immediately
            user = form.save(commit=False)
            # Convert plain password into hashed password
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("signin")
    else:
        form = UserForm()
    return render(request, "signup.html", {"form": form})


def signin_view(request):
    if request.method == "POST":
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("upload_pdf")
    else:
        form = SignInForm()
    return render(request, "signin.html", {"form": form})


def home(request):
    return render(request, "home.html")


def upload_pdf(request):

    #   extracted_text = ""

    if request.method == "POST":

        file = request.FILES["file"]

        document = Document.objects.create(file=file)

        pdf_path = document.file.path

        # Load PDF
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

        chunks = splitter.split_documents(documents)

        # Create embeddings
        embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Convert to vectors
        vectors = embedding.embed_documents(
            [chunk.page_content or "" for chunk in chunks]
        )

        # Save FAISS index
        db = FAISS.from_documents(chunks, embedding)

        db.save_local("faiss_index")

        # # Display chunk text safely
        # for i, chunk in enumerate(chunks):

        #     extracted_text += (
        #         f"\n\n----- Chunk {i+1} -----\n"
        #     )

        #     extracted_text += (
        #         chunk.page_content or ""
        #     )

        # extracted_text += (
        #     f"\n\nTotal vectors created: {len(vectors)}"
        # )

        # extracted_text += (
        #     "\n\nFAISS index created successfully"
        # )

        return redirect("chat")

    return render(
        request,
        "file_upload.html",
        # {
        #     "text": extracted_text
        # }
    )


def chat(request):

    answer = ""
    question = ""

    if request.method == "POST":

        question = request.POST["question"]

        embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        db = FAISS.load_local(
            "faiss_index", embedding, allow_dangerous_deserialization=True
        )

        results = db.similarity_search(question, k=3)

        context = ""

        for result in results:
            context += result.page_content + "\n"

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", google_api_key=settings.GEMINI_API_KEY
        )

        response = llm.invoke(f"""
            Answer only using the provided context.

            Context:
            {context}

            Question:
            {question}
            """)

        answer = response.content

    return render(request, "chat.html", {"question": question, "answer": answer})
