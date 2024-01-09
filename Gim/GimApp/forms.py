from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class CustomRegistrationForm(UserCreationForm):
    profile_picture = forms.ImageField(label='Imagen de Perfil', required=False)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'profile_picture')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']