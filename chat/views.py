from django.shortcuts import render ,redirect
from .models import Question,Answers 
from .forms import QuestionForm,Answersform



def question_list(request):
    question = Question.objects.all()
    return render(request,'chat/question.html',{'que':question})

def question_detail(request,id):
    question = Question.objects.get(id=id)
    answer = Answers.objects.filter(question=question)

    if request.method == 'POST':
        form = Answersform(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.author = request.user
            my_form.question = question
            my_form.save()
    else:
        form = Answersform()
    
    return render(request,'chat/detail.html',{'que':question,
                                              'ans':answer,
                                              'form':form})


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


def answer_delete(request,id):
    delete = Answers.objects.get(id=id)
    delete .delete()
    return redirect(f'/chat/{delete.question.id}')


