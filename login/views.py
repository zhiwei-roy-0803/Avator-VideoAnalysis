from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# 登录界面
from django.views.decorators.csrf import csrf_protect
from .form import RegisterForm

def UserLogin(request):
    received_data = request.POST
    if len(received_data) == 0:
        return render(request, 'login/login.html', context={"message": "Please Enter Username and Password!"})
    username = received_data["username"]
    password = received_data["password"]
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect("video:home", username=username)
    else:
        return render(request, 'login/login.html', context={"message": "Login Fail! Wrong Username or Password!"})

# 注册界面
def UserRegister(request):
    received_data = request.POST
    if len(received_data) == 0:
        register_form = RegisterForm()
        return render(request, "login/register.html", context={"message": "Enter User Information",
                                                               "register_form": register_form})
    username = received_data["username"]
    password1 = received_data["password1"]
    password2 = received_data["password2"]
    email = received_data["email"]
    if password1 == password2:
        same_name_user = User.objects.filter(username=username)
        same_email = User.objects.filter(email=email)
        if same_name_user:
            return render(request, 'login/login.html', context={"message": "Already Exist User!"})
        elif same_email:
            return render(request, 'login/login.html', context={"message": "Already Exist E-mail!"})
        else:
            user = User(username=username, email=email)
            user.set_password(raw_password=password1)
            user.save()
            return render(request, 'login/login.html', context={"message": "Register Finished"})
    else:
        return render(request, 'login/register.html', context={"message": "Password1 Does Not Match Password2"})

# 登出界面
def UserLogOut(request):
    logout(request)
    return render(request, 'login/login.html', context={"message": "You Have Logged Out!"})
