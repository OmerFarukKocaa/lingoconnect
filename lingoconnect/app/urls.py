from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path("quizes/",views.Quizes,name="quizes"),
    path("Quiz/<int:quiz_id>/",views.quiz,name="Quiz"),
    path('submit-quiz/<int:quiz_id>/',views.submit_quiz,name='submit_quiz'),

]
