from django.urls import path 
from . import views , views2

app_name = 'chat'
 
#   chat/
urlpatterns = [
    path('' , views.question_list,name='ques_list'),
    path('<int:id>' , views.question_detail , name = 'question_detail'),
    path('add/' , views.question_add , name = 'question_add'),
    path('<int:id>/delete/' , views.qusetion_delete , name = 'qusetion_delete'),
    path('<int:id>/ans_delate' , views.answer_delete , name = 'answer_delete'),
    path('edit/<int:id>' , views.question_edit , name ='question_edit'),
    path('<int:id>/edit' , views.answer_edit , name = 'answer_edit'),

    path('gen/' , views2.QiestionList.as_view()),
    path('gen/<int:pk>/' , views2.QuestionDetail.as_view()),
    path('gen/<int:id>/delete/' , views2.QuestionDelete.as_view()),
]


