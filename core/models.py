from django.db import models


# Create your models here.

####################  Опросы  ####################

class PollsDB(models.Model):
    """ Опросы """
    name_poll = models.CharField(max_length=200, verbose_name="Название опроса", null=False)
    description_text = models.TextField(verbose_name="Описание опроса", blank=True, null=True)
    date_start = models.DateField('Дата начала')
    date_end = models.DateField('Дата окончания')

    class Meta:
        ordering = ['date_start']
        verbose_name = u'Опрос'
        verbose_name_plural = u'Опросы'

    def __str__(self):
        return self.name_poll


class Questions(models.Model):
    """ Вопросы для опросов """
    polls_id = models.ForeignKey(PollsDB, on_delete=models.CASCADE, related_name="questions",
                                 verbose_name="Название опроса")
    question_text = models.TextField(verbose_name="Текст вопроса", null=False)
    TYPE_CHOICES = (
        ('S', 'Один ответ'),
        ('M', 'Несколько ответов'),
        ('T', 'Ответ текстом'),)
    type_quest = models.CharField('Варианты ответов', max_length=1, blank=False, choices=TYPE_CHOICES,
                                  default='S',
                                  null=False)

    class Meta:
        ordering = ['polls_id']
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'

    def __str__(self):
        return self.question_text


class Answers(models.Model):
    """ Ответы для вопросов """
    quest_id = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.CharField(max_length=200, verbose_name="Текст ответа", null=True)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['quest_id']
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'

    def __str__(self):
        return self.answer_text


####################  Ответы пользователей  ####################

class Users(models.Model):
    """ Пользователи проходившие опросы """
    user_id = models.BigIntegerField(default=1)
    user_ip = models.CharField(max_length=20, default='127.0.0.1')


class UserAnswer(models.Model):
    """ Ответы пользователя """
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE, default=1, related_name="users")
    id_polls = models.ForeignKey(PollsDB, on_delete=models.CASCADE, related_name="user_polls")
    id_quest = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="user_questions")
    id_answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name="user_answers")
    answer_text = models.CharField(max_length=200,
                                   verbose_name="Текст ответа пользователя, если выбран текстовый ответ", null=True)
