from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Register

class SignupForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'username', 'email', 'password', 'confirm_password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            'username',
            'password'
        ]