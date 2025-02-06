from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from rest_framework.authtoken.views import ObtainAuthToken, Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def userList(request):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


############ SIGNUP/LOGIN ############

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
        return render(request, 'userauth/login.html',{})