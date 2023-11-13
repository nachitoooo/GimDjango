from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_clientes/', views.agregar_clientes, name='agregar_clientes'), 
]
