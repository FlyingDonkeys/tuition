from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question_sender = models.ForeignKey(User, on_delete=models.CASCADE)
    question_description = models.TextField(max_length=500)
    question_image = models.ImageField(upload_to='Questions/static/images/')
    is_solved = models.BooleanField(default=False)


class Answer(models.Model):
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer")
    answer_provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="solves")
    answer_description = models.TextField(max_length=500)
    answer_image = models.ImageField(upload_to='Questions/static/images/')


