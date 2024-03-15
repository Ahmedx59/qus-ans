from django.shortcuts import render
from .models import Question,Answers 


def question_list(request):
    question = Question.objects.all()
    return render(request,'chat/question.html',{question:'que'})
