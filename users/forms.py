from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.forms.widgets import DateInput

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(forms.ModelForm):
    '''Simple login form'''
    class Meta:
        model = User
        fields = ['username', 'password']

class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['img', 'gender', 'cnic', 'phoneNo', 'address', 'dateOfBirth']
        labels = {
            'dateOfBirth': ('D.O.B'),
        }
        widgets = {
            'dateOfBirth': DateInput(attrs={'type':'date'})
        }