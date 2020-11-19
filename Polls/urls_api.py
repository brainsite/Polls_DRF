from django.urls import include, path
from rest_framework import routers

from core import views_rest

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path("polls/", views_rest.PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", views_rest.PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/quest/", views_rest.QuestList.as_view(), name="choice_list"),
    path("polls/<int:pk>/quest/<int:quest_pk>/answer/", views_rest.AnswersList.as_view(), name="choice_quest"),
    path("polls/<int:pk>/quest/<int:quest_pk>/answer/<int:choice_pk>/vote/", views_rest.CreateVote.as_view(), name="create_vote"),

    path("user_polls/", views_rest.UserPollsList.as_view(), name="user_polls_list"),


]
