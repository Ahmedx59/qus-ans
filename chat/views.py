from django.shortcuts import render ,redirect
from .models import Question,Answers 
from .forms import QuestionForm,AnswersForm



def question_list(request):
    question = Question.objects.all()
    return render(request,'chat/question_list.html',{'que':question})

def question_detail(request,id):
    question = Question.objects.get(id=id)
    answer = Answers.objects.filter(question=question)

    if request.method == 'POST':
        form = AnswersForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.author = request.user
            my_form.question = question
            my_form.save()
    else:
        form = AnswersForm()  
    return render(request,'chat/question_detail.html',{'que':question,
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

def answer_edit(request,id):
    answer = Answers.objects.get(id=id)
    if request.method == 'post':
        form = AnswersForm(request.POST , instance=answer)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.outhor = request.user
            my_form.save()
            return redirect(f'/chat/{answer.id}')
    else :
        form =AnswersForm(instance=answer)
    return render(request , 'chat/add.html',{'form':form})



def answer_delete(request,id):
    delete = Answers.objects.get(id=id)
    delete .delete()
    return redirect(f'/chat/{delete.question.id}')

def question_edit(request,id):
    question =  Question.objects.get(id=id)
    if request.method == 'POST':
        form = QuestionForm(request.POST,instance=question)
        if form.is_valid():
            form.save()
            return redirect(f'/chat/{question.id}')
    else:
        form = QuestionForm(instance=question)
    return render(request,'chat/add.html',{'form':form})






