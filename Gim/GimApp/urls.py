from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('gestionar_clientes/', views.gestionar_clientes, name='gestionar_clientes'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
