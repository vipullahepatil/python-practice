from django.urls import path

from polls.views import QuestionListCreateAPIView, question_list

  

urlpatterns = [
    path('', question_list, name='question_list'),
]

urlpatterns = [
    path('api/questions/', QuestionListCreateAPIView.as_view(), name='api_questions'),
]