from django.urls import path 
from .views import question_list

app_name = 'chat'
 
#   chat/
urlpatterns = [
    path('question/',question_list,name='ques_list'),
    
]


