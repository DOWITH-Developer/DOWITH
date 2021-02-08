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
from django.core.serializers import json
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


# Forbidden (CSRF token missing or incorrect.) 문제로 데코레이터 추가함
@csrf_exempt
def userinfo_get(request):
    user_name = request.user.username
    user_nickname = request.user.nickname
    user_email = request.user.email
    return JsonResponse({"name": user_name, "nickname": user_nickname, "email": user_email})


@csrf_exempt
def userchallenge_get(request):
    # user의 challenge 접근하는 문법(쿼리셋?) 공부하기
    # user = User.objects.get(nickname="jmchoi")
    # challenges = user.player_set.all()
    # challenge_name = user.player_set.get().challenge.title -> a
    user = request.user
    challenge_enrollments = user.chEnrollment_set.all()
    challenge_enrollments_len = len(challenge_enrollments)
    challenge_titles = []
    for i, ch in enumerate(list(challenge_enrollments)):
        print(ch.challenge.title)
        print(ch.challenge.pk)
        print(ch.challenge)
        challenge_titles.append(ch.challenge)
        # challenge_titles.append([ch.challenge.pk, ch.challenge.title])
    # print(challenge_titles)
    json_serializer2 = json.Serializer()
    json_serialized2 = json_serializer2.serialize(challenge_titles)
    print(json_serialized2)

    print(challenge_enrollments)
    print(challenge_enrollments[0].challenge.pk)
    json_serializer = json.Serializer()
    json_serialized = json_serializer.serialize(challenge_enrollments)
    # print(json_serialized)
    # print(len(challenge_enrollments))
    return JsonResponse({"ch_enrollments": json_serialized, "ch_enrollments_len": challenge_enrollments_len, "ch_titles": json_serialized2})


@csrf_exempt
def usersetting_get(request):
    # 설정사항들 정하고 모델에 필드 추가하기
    return JsonResponse({})
