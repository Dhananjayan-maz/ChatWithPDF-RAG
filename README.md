# 📄 AI Document Question Answering System using RAG

An AI-powered document assistant that enables users to upload PDF documents and ask questions based on uploaded content. The system uses a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant information and generate context-aware responses.

---
## 🚀 Project Overview

Traditional language models generate responses based on pre-trained knowledge and may produce inaccurate information for domain-specific documents.

This project addresses that limitation using Retrieval-Augmented Generation (RAG), where relevant information is first retrieved from uploaded documents and then passed to a Large Language Model (LLM) to generate accurate answers.

The application allows users to:

- Upload PDF documents
- Extract and process document text
- Generate vector embeddings
- Store vectors in a FAISS database
- Perform semantic search
- Generate AI-powered responses using Gemini

---

## ✨ Features

✅ PDF upload support  
✅ Automatic text extraction  
✅ Text chunking for large documents  
✅ Embedding generation using HuggingFace  
✅ Vector storage using FAISS  
✅ Semantic similarity search  
✅ Context-aware response generation  
✅ Interactive AI chat interface  
✅ End-to-end RAG workflow  

---

## 🛠 Technologies Used

### Frontend
- HTML
- CSS

### Backend
- Django
- Python

### AI & Libraries
- LangChain
- HuggingFace Embeddings
- Gemini API
- PyPDF
- FAISS Vector Database

### Tools
- VS Code
- GitHub

---

## ⚙️ System Workflow

```text
User Uploads PDF
        ↓
PDF Text Extraction
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
Store Embeddings in FAISS
        ↓
User asks Question
        ↓
Convert Question → Vector
        ↓
Similarity Search
        ↓
Retrieve Relevant Chunks
        ↓
Gemini Generates Response
```

---

## 🧠 Project Architecture

```text
                ┌─────────────────┐
                │ Upload PDF File │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Extraction │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Chunking   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Embedding Model │
                │ HuggingFace     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ FAISS Vector DB │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Similarity      │
                │ Search          │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Gemini LLM      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Generated Answer│
                └─────────────────┘
```

## 📦 Installation

Clone repository:

```bash
git clone https://github.com/Dhananjayan-maz/ChatWithPDF-RAG.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Install dotenv:

```bash
pip install python-dotenv
```

---

## 📷 Project Screenshots

<img width="1893" height="910" alt="home_rag" src="https://github.com/user-attachments/assets/7468bab9-53e6-4a7f-8b00-1ff79481754b" />

<img width="1915" height="912" alt="upload_rag" src="https://github.com/user-attachments/assets/dedb1431-206f-4993-a4f4-0d0d1f916b06" />

<img width="1917" height="902" alt="chat_rag" src="https://github.com/user-attachments/assets/bcc5d37c-322f-4ee2-8ce3-f20c1d739f66" />

---

## 🎯 Future Enhancements

- Multiple PDF support
- Conversation history
- Duplicate PDF detection
- Cloud deployment
- Source citations for responses

---
