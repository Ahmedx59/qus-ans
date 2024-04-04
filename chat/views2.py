from .models import Question , Answers
from django.views import generic



class QiestionList(generic.ListView):
    model = Question


class QuestionDetail(generic.DetailView):
    model = Question


class QuestionDelete(generic.DeleteView):
    model = Question

