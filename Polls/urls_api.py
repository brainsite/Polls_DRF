from django.urls import include, path
from rest_framework import routers

from core import views_rest

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),


    path('polls/', views_rest.PollsListAPIViews.as_view()),

    # FOR ADMINS
    path('polls_all/', views_rest.PollsAdminsListAPIView.as_view()),
    path('polls_all/<int:pk>/', views_rest.PollsAdminsDetailAPIView.as_view()),
    path('questions/<int:pk>/', views_rest.QuestionsAdminsDetailAPIView.as_view()),
    path('answer/<int:pk>/', views_rest.AnswerAdminsDetailAPIView.as_view()),

    # ADD URLS
    path("add_polls/", views_rest.AddPollsView.as_view()),
    path("add_questions/", views_rest.AddQuestionsView.as_view()),
    path("add_answer/", views_rest.AddAnswerView.as_view()),

]
