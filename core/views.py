from django.shortcuts import render

# Create your views here.

def index(request):
    """ Главная страница """
    lists = {'id':request.session}
    return render(request, 'index.html', lists)