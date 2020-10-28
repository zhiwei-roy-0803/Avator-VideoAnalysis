from django.conf.urls import url
from .views import *

urlpatterns = [
    url('login/', UserLogin, name="login"),
    url('register/', UserRegister, name="register"),
    url('logout/', UserLogOut, name="logout"),
]