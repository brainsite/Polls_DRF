# Polls_DRF
Тестовое задание "Спроектировать и разработать API для системы опросов пользователей"

# Инструкция для API

Рабочая версия http://poll.brainsite.ru 
API сайта http://poll.brainsite.ru/api 

Список активных опросов:
http://poll.brainsite.ru/api/polls/

Список всех опросов (для админа):
http://poll.brainsite.ru/api/polls_all/

Изменение опроса (для админа):
http://poll.brainsite.ru/api/polls_all/<int:pk>/  где <int:pk> это ID опроса

Изменение вопроса (для админа):
http://poll.brainsite.ru/api/questions/<int:pk>/  где <int:pk> это ID вопроса

Изменение ответов (для админа):
http://poll.brainsite.ru/api/answer/<int:pk>/  где <int:pk> это ID ответа

Добавить опрос:
http://poll.brainsite.ru/api/add_polls/

Добавить вопрос:
http://poll.brainsite.ru/api/add_questions/

Добавить ответ:
http://poll.brainsite.ru/api/add_answer/
