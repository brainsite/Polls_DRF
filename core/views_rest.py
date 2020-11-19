from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import PollsDB, Questions, Answers, UserAnswer, Users
from .serializers import PollsSerializer, AnswerSerializer, UserAnswerSerializer, QuestionsSerializer, UserAnsSerializer
from .utils import get_client_ip


class PollList(generics.ListCreateAPIView):
    """Список всех опросов"""
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            raise PermissionDenied("You can not create poll.")
    queryset = PollsDB.objects.all()
    serializer_class = PollsSerializer


class UserPollsList(generics.ListAPIView):
    """Список ответов пользователя"""

    def get_queryset(self):
        queryset = UserAnswer.objects.filter(id_user__user_ip=get_client_ip(self.request))
        return queryset

    serializer_class = UserAnsSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    """Опрос подробно"""
    queryset = PollsDB.objects.all()
    serializer_class = PollsSerializer


class QuestList(generics.ListCreateAPIView):
    """Список вопросов в опросе"""

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            raise PermissionDenied("You can not create questions for this poll.")

    def get_queryset(self):
        queryset = Questions.objects.filter(polls_id=self.kwargs["pk"])
        return queryset

    serializer_class = QuestionsSerializer


class AnswersList(generics.ListCreateAPIView):
    """ Список ответов для вопроса """

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            raise PermissionDenied("You can not create answer for this question.")

    def get_queryset(self):
        queryset = Answers.objects.filter(quest_id=self.kwargs["pk"])
        return queryset

    serializer_class = AnswerSerializer


class CreateVote(APIView):
    """ Голосование """
    serializer_class = UserAnswerSerializer

    def post(self, request, pk, quest_pk, choice_pk):
        try:
            user_id = Users.objects.get(user_ip=get_client_ip(request))
        except:
            new_user_id = int(''.join(filter(lambda i: i.isdigit(), get_client_ip(request))))
            print(new_user_id)
            user_id = Users(user_ip=get_client_ip(request), user_id=new_user_id)
            user_id.save()
        data = {'id_answer': choice_pk, 'id_quest': quest_pk, 'id_polls': pk, 'id_user': user_id.id}
        serializer = UserAnswerSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
