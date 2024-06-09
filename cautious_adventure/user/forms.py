from django.forms import ModelForm, Form, CharField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import Profile


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', "password2"]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['prof_username', 'prof_name', 'prof_email', 'prof_photo']
        labels = {
            'prof_username': 'Username',
            'prof_name': 'Name',
            'prof_email': 'Email',
            'prof_photo': 'Photo'
        }


class LoginForm(Form):
    username = CharField(label='Username', max_length=100)
    password = CharField(widget=PasswordInput)
    captcha = CaptchaField(label="")

    