from django.db import models
from django.contrib.auth import get_user_model



class Document(models.Model):
    file=models.FileField(upload_to='documents/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

