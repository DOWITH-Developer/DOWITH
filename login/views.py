from django.shortcuts import render, redirect
from .models import *
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_user
# Create your views here.


def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # username_id = User.id
            # user = User.objects.create(
            #     username=username_id,
            #     email=request.POST["email"],
            #     nickname=request.POST["nickname"],
            #     password=request.POST["password1"]
            # )
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
            auth_user(request, user)
            return redirect("login:test")
        else:
            ctx = {
                "error": "email or password is incorrect",
            }
            return render(request, "login/login.html", ctx)
    if request.method == "GET":
        form = LoginForm()
        ctx = {
            "form": form,
        }
        return render(request, "login/login.html", ctx)
