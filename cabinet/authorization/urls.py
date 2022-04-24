from django.urls import path
from . import views

urlpatterns = [
    # Страница авторизации
    path('', views.index),
]
