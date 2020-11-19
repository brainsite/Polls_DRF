import datetime

from rest_framework import serializers

from .models import PollsDB, Questions, Answers, UserAnswer, Users


class FilterActivePollSerializer(serializers.ListSerializer):
    """Фильтр опросов, только активные"""

    def to_representation(self, data):
        data = data.filter(date_end__gt=datetime.date.today())
        return super().to_representation(data)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Questions
        fields = '__all__'


class PollsSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True, required=False)

    class Meta:
        list_serializer_class = FilterActivePollSerializer
        model = PollsDB
        fields = '__all__'


class UserAnswerSerializer(serializers.ModelSerializer):
    # user_polls = PollsSerializer(many=True)
    class Meta:
        model = UserAnswer
        fields = '__all__'


class UserAnsSerializer(serializers.ModelSerializer):
    id_polls = serializers.SlugRelatedField(slug_field="name_poll", read_only=True, help_text='Название опроса')
    id_quest = serializers.SlugRelatedField(slug_field="question_text", read_only=True, help_text='Вопрос')
    id_answer = serializers.SlugRelatedField(slug_field="answer_text", read_only=True, help_text='Ответ')

    class Meta:
        model = UserAnswer
        fields = '__all__'
