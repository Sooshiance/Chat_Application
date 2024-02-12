from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': "Username",
            'email': "Email",
            'password1': "Password",
            'password2': "Password confirm",
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control my-5'}),
            'email': forms.EmailInput(attrs={'class':'form-control my-5'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control my-5'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control my-5'}),
        }
