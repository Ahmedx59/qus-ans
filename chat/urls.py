from django.urls import path 
from . import views

app_name = 'chat'
 
#   chat/
urlpatterns = [
    path('',views.question_list,name='ques_list'),
    path('detail/<int:id>' , views.question_detail , name = 'question_detail')

]


