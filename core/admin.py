from django.contrib import admin

from core.models import PollsDB, Questions, Answers


# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    fields = ['quest_id', 'answer_text']

class AnswerlineAdmin(admin.StackedInline):
    model = Answers

class QuestionslineAdmin(admin.StackedInline):
    model = Questions

class QuestionsAdmin(admin.ModelAdmin):
    fields = ['polls_id', 'question_text', 'type_quest']
    inlines = [AnswerlineAdmin, ]

class PollsDBAdmin(admin.ModelAdmin):
    fields = ['name_poll', 'description_text', 'date_start', 'date_end']
    list_display = ('name_poll', 'date_start', 'date_end')
    list_filter = ['name_poll', 'date_start', 'date_end']
    inlines = [QuestionslineAdmin, ]







admin.site.register(Questions,QuestionsAdmin)
admin.site.register(Answers,AnswerAdmin)
admin.site.register(PollsDB,PollsDBAdmin)