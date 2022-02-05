from email.mime import image
from time import timezone
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Resume(models.Model):
    Age = models.CharField(max_length=30)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=30)
    Skype = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Langages = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=30)
    Nationality = models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30, default="Disponible")

    def __str__(self):
        return f"{self.LastName} --- {self.FirstName}"


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title




