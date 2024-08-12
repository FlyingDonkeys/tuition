from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question_sender = models.ForeignKey(User, on_delete=models.CASCADE)
    question_description = models.TextField(max_length=500)
    question_image = models.ImageField(upload_to='images/')


