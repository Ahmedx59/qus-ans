from django.shortcuts import render ,redirect
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
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.author = request.user
            my_form.save()
            return redirect('/chat/')
    else:
        form = QuestionForm()
    return render(request,'chat/add.html',{'form':form})

def qusetion_delete(request,id):
    delet = Question.objects.get(id=id)
    delet.delete()
    return redirect('/chat/')





