from rest_framework import generics
from rest_framework import permissions

from core.serializers import PollsSerializer, PollsDetailSerializer, CreateQuestionsSerializer, PollsAdminSerializer, \
    CreateAnswerSerializer, CreatePollsSerializer, QuestionsAdminSerializer, AnswerAdminSerializer
from .models import PollsDB, Questions, Answers


class PollsAdminsListAPIView(generics.ListAPIView):
    """Все опросы"""
    queryset = PollsDB.objects.all().order_by('-date_start')
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollsAdminsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Изменение опроса для Админа"""
    queryset = PollsDB.objects.all().order_by('-date_start')
    serializer_class = PollsAdminSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionsAdminsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Изменение вопроса для Админа"""
    queryset = Questions.objects.all().order_by('id')
    serializer_class = QuestionsAdminSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnswerAdminsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Изменение ответа для Админа"""
    queryset = Answers.objects.all().order_by('id')
    serializer_class = AnswerAdminSerializer
    permission_classes = [permissions.IsAuthenticated]

class PollsListAPIViews(generics.ListAPIView):
    """Все активные опросы"""
    queryset = PollsDB.objects.all().order_by('-date_start')
    serializer_class = PollsDetailSerializer

class AddPollsView(generics.CreateAPIView):
    """Добавление опроса"""
    serializer_class = CreatePollsSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddQuestionsView(generics.CreateAPIView):
    """Добавление вопроса к опросу"""
    serializer_class = CreateQuestionsSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddAnswerView(generics.CreateAPIView):
    """Добавление ответов к вопросу"""
    serializer_class = CreateAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]
