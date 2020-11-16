import datetime

from rest_framework import serializers

from .models import PollsDB, Questions, Answers


class FilterActivePollSerializer(serializers.ListSerializer):
    """Фильтр опросов, только активные"""

    def to_representation(self, data):
        data = data.filter(date_end__gt=datetime.date.today())
        return super().to_representation(data)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id', 'answer_text']


class QuestionsSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Questions
        fields = ['id', 'question_text', 'type_quest', 'answers']


class PollsSerializer(serializers.ModelSerializer):
    """Serializer Опросов для Админа"""
    questions = QuestionsSerializer(many=True)

    class Meta:
        model = PollsDB
        fields = ['id', 'name_poll', 'description_text', 'date_start', 'date_end', 'questions']


class PollsAdminSerializer(serializers.ModelSerializer):
    """DetailSerializer Опросов для Админа"""

    class Meta:
        model = PollsDB
        fields = ['id', 'name_poll', 'description_text', 'date_start', 'date_end']

class QuestionsAdminSerializer(serializers.ModelSerializer):
    """DetailSerializer Вопросов для Админа"""

    class Meta:
        model = Questions
        fields = ['id', 'polls_id', 'question_text', 'type_quest']

class AnswerAdminSerializer(serializers.ModelSerializer):
    """DetailSerializer Ответов для Админа"""

    class Meta:
        model = Answers
        fields = ['id', 'quest_id', 'answer_text']

class PollsDetailSerializer(serializers.ModelSerializer):
    """Serializer Опросов для всех"""
    questions = QuestionsSerializer(many=True)

    class Meta:
        list_serializer_class = FilterActivePollSerializer
        model = PollsDB
        fields = ['id', 'name_poll', 'description_text', 'date_start', 'date_end', 'questions']


class CreatePollsSerializer(serializers.ModelSerializer):
    """Добавление опроса"""

    class Meta:
        model = PollsDB
        fields = ('name_poll', 'description_text', 'date_start', 'date_end')

    def create(self, validated_data):
        polls, _ = PollsDB.objects.update_or_create(
            name_poll=validated_data.get('name_poll', None),
            description_text=validated_data.get('description_text', None),
            date_start=validated_data.get('date_start', None),
            date_end=validated_data.get('date_end', None),
        )
        return polls

class CreateQuestionsSerializer(serializers.ModelSerializer):
    """Добавление вопросов к опросу"""

    class Meta:
        model = Questions
        fields = ("polls_id", "question_text", "type_quest")

    def create(self, validated_data):
        question, _ = Questions.objects.update_or_create(
            question_text=validated_data.get('question_text', None),
            polls_id=validated_data.get('polls_id', None),
            type_quest=validated_data.get('type_quest', None),
        )
        return question


class CreateAnswerSerializer(serializers.ModelSerializer):
    """Добавление ответов к вопросу"""

    class Meta:
        model = Answers
        fields = ("quest_id", "answer_text")

    def create(self, validated_data):
        answer, _ = Answers.objects.update_or_create(
            answer_text=validated_data.get('answer_text', None),
            quest_id=validated_data.get('quest_id', None),
        )
        return answer
