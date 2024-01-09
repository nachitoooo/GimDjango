from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomRegistrationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'GimApp/index.html')

def gestionar_clientes(request):
    return render (request, 'GimApp/gestionar_clientes.html')

def login(request):
    return render(request, 'GimApp/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile, created = Profile.objects.get_or_create(user=user)
            if 'profile_picture' in request.FILES:
                profile.profile_image = request.FILES['profile_picture']
                profile.save()
            return redirect('index')
    else:
        form = CustomRegistrationForm()
    return render(request, 'GimApp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    else:
        form = AuthenticationForm()
    return render(request, 'GimApp/index.html', {'form': form})