from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ваше имя', 'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Введите пароль', 'class':'form-control'}))
    class Meta:
        model=User
        fields=['username', 'password']