from django import forms
from .models import Question,Answers

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['author']


class Answersform(forms.ModelForm):
    class Meta:
        model = Answers
        exclude = ['author']