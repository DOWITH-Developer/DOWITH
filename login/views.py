import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #다른 경로 모델 import위해

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from challenge.models import * # Enrollment가져옴
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login:test")
        else:
            ctx = {
                "form": form,
            }
            return render(request, "login/signup.html", ctx)
    elif request.method == "GET":
        form = SignUpForm()
        ctx = {
            "form": form,
        }
        return render(request, "login/signup.html", ctx)


def test(request):
    return render(request, "login/layout.html")


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("login:test")
        else:
            ctx = {
                "error": "email or password is incorrect",
            }
            return render(request, "login/login.html", ctx)
    elif request.method == "GET":
        form = LoginForm()
        ctx = {
            "form": form,
        }
        return render(request, "login/login.html", ctx)


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("login:test")
    elif request.method == "GET":
        return redirect("login:test")

def my_page(request, pk):
    me = get_object_or_404(User, id=pk) #me = 접속한 user
    friends = me.self_set.all() #me의 friend들
    enrollments = Enrollment.objects.filter(
            player=me)
    ctx = {        
        'me': me,
        'friends': friends,
        'enrollments' : enrollments,
    }
    return render(request, "login/mypage.html", ctx)