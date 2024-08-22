from django.db import models
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
from django import forms
class loginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)
