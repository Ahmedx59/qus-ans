from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
TAG_OPTIONS = (
    ('Old','Old'),
    ('New','New')
)

class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='user_question')
    question = models.CharField(max_length=200)
    tags = models.CharField(max_length=50, choices=TAG_OPTIONS)
    created_at = models.DateField(default=timezone.now)
    content = models.TextField(max_length=1000)


class Answers(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='author_answer')
    answer = models.TextField(max_length=1000)
    question = models.ForeignKey(Question,on_delete=models.CASCADE , related_name='question_answer')
    created_at = models.TimeField(default=timezone.now)