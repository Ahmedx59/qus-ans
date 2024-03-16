from django.shortcuts import render
from .models import Question,Answers 
from .forms import QuestionForm



def question_list(request):
    question = Question.objects.all()
    return render(request,'chat/question.html',{'que':question})

def question_detail(request,id):
    question = Question.objects.get(id=id)
    answer = Answers.objects.filter(question=question)
    return render(request,'chat/detail.html',{'que':question,'ans':answer})

def question_add(request):
    form = QuestionForm()
    return render(request,'chat/add.html',{'form':form})