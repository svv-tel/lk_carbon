from django.http import HttpResponse
from django.shortcuts import render


# Страница авторизации
def index(request):
    template = 'ice_cream/index.html'
    return HttpResponse('Главная страница')
