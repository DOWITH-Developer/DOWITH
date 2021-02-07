from django.shortcuts import render, redirect
from .models import *
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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
                "form": form,
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


# settings
@login_required
def settings_main(request):
    return render(request, "login/settings_main.html")


# class UserInfo(View):
#     template_name = "login/settings_main.html"

#     # 포비든 문제때문에 추가
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(LikeAjax, self).dispatch(request, *args, **kwargs)

#     def post(self, request):
#         user_name = request.user.username
#         user_nickname = request.user.nickname
#         user_email = request.user.email

#         return JsonResponse({"user":})
