from django import forms
from .models import student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class detailsfrom(forms.ModelForm):
    class Meta:
        model=student
        fields=("email","name","ph")
class createForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter your password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter your password'}))
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
