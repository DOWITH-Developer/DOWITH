from django.shortcuts import render, redirect
from .models import *
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.


def signUp(request):
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
