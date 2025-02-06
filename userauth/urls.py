from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token
from . import views 

urlpatterns = [
    path('user_list/',views.userList),
    path('get_token/<int:id>/',obtain_auth_token),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
]