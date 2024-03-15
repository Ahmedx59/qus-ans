from django.shortcuts import render
from .models import Question,Answers 


def question_list(request):
    question = Question.objects.all()
    return render(request,'chat/question.html',{'que':question})

def question_detail(request,id):
    question = Question.objects.get(id=id)
    return render(request,'chat/detail.html',{'que':question})