from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token
from . import views 

urlpatterns = [
    path('get_token/<int:id>/',obtain_auth_token),
    path('',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
]