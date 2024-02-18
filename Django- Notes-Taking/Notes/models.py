from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    def __str__(self):
        return self.username

class Note(models.Model):
    title = models.CharField(max_length=35)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Using string reference to handle forward reference
    def __str__(self):
        return f"{self.title} - {self.content}"

