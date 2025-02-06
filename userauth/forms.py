from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','id':'email','placeholder':'Enter Email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','id':'username','placeholder':'Enter Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','id':'password','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['email','username', 'password1','password2']