from django.urls import path 
from . import views

app_name = 'chat'
 
#   chat/
urlpatterns = [
    path('',views.question_list,name='ques_list'),
    path('<int:id>' , views.question_detail , name = 'question_detail'),
    path('add/', views.question_add , name = 'question_add'),
    path('<int:id>/delete/', views.qusetion_delete , name = 'qusetion_delete'),
    path('<int:id>/ansdelate',views.answer_delete , name = 'answer_delete'),
    

]


