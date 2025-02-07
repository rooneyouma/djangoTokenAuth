from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from rest_framework.authtoken.views import ObtainAuthToken, Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework.exceptions import AuthenticationFailed


def signup(request):
        if request.method == 'POST':
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('login')
                else:
                        print(form.errors)
        else:
                form = CustomUserCreationForm()



        return render(request, 'userauth/signup.html',{'form':form})

def login(request):

        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = authenticate(request, username=username, password=password)

                if user is not None:
                        token, created = Token.objects.get_or_create(user=user)
                        return redirect('home')
                else:
                        messages.error(request,"Invalid credentials")
                        return redirect('login')

        return render(request, 'userauth/login.html',{})

def home(request):
        return render(request, 'userauth/home.html')