from django.core.serializers import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .forms import SignUpForm, LoginForm, UserInfoModifyForm, UserPasswordChangeForm
from challenge.models import *  # Enrollment가져옴
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    os.path.dirname(__file__))))  # 다른 경로 모델 import위해

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("challenge:ch_list")
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
            return redirect("challenge:ch_list")
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


def my_page(request, pk):
    me = get_object_or_404(User, id=pk)  # me = 접속한 user
    friends = me.self_set.all()  # me의 friend들
    enrollments = Enrollment.objects.filter(
        player=me)
    ctx = {
        'me': me,
        'friends': friends,
        'enrollments': enrollments,
    }
    return render(request, "login/mypage.html", ctx)

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
    user_is_social = request.user.is_social
    return JsonResponse({"name": user_name, "nickname": user_nickname, "email": user_email, "is_social": user_is_social})


@csrf_exempt
def userchallenge_get(request):
    user = request.user
    user_enrollment_list = user.chEnrollment_set.all()  # user의 enrollment list
    user_challenge_list = []    # user가 참여한 challenge list

    # enrollment list 직렬화 --> QuerySet을 json으로 변환
    enrollment_list_serializer = json.Serializer()
    enrollment_list_serialized = enrollment_list_serializer.serialize(
        user_enrollment_list)

    # user가 참여한 challenge를 user_enrollment_list를 통해 가져와 list로 담음
    for i, ch in enumerate(list(user_enrollment_list)):
        user_challenge_list.append(ch.challenge)

    # challenge list 직렬화 --> QuerySet을 json으로 변환
    challenge_list_serializer = json.Serializer()
    challenge_list_serialized = challenge_list_serializer.serialize(
        user_challenge_list)

    return JsonResponse({"enrollment_list": enrollment_list_serialized, "challenge_list": challenge_list_serialized})


@csrf_exempt
def usersetting_get(request):
    # 설정사항들 정하고 모델에 필드 추가하기
    return JsonResponse({})


# settings 2차
def userinfo_modify(request):
    if request.method == "POST":
        form = UserInfoModifyForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("login:settings")
        else:
            ctx = {
                "form": form,
            }
            return render(request, "login/userinfo_modify.html", ctx)
    elif request.method == "GET":
        form = UserInfoModifyForm(instance=request.user)
        ctx = {
            "form": form,
        }
        return render(request, "login/userinfo_modify.html", ctx)


def userinfo_password_modify(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("login:login")
        else:
            ctx = {
                "form": form,
            }
            return render(request, "login/userpassword_modify.html", ctx)
    if request.method == "GET":
        form = UserPasswordChangeForm(request.user)
        ctx = {
            "form": form,
        }
        return render(request, "login/userpassword_modify.html", ctx)
