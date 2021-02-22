from django.core.serializers import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .forms import SignUpForm, LoginForm, UserInfoModifyForm, UserPasswordChangeForm, UserImageModifyForm, SocialSignUpForm
from challenge.models import *  # Enrollment가져옴
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(
    os.path.dirname(__file__))))  # 다른 경로 모델 import위해

# from django.contrib.auth.forms import UserCreationForm

import json as JSON
from datetime import date #today가져오기 위해
from django.template.defaulttags import register

# decorator
from .decorators import allowed_users, required_login
# from django.contrib.auth.decorators import login_required


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login:signup_success")
        else:
            error_nickname_same = ""

            if form.non_field_errors():
                error_nickname_same = "사용자의 닉네임은/는 이미 존재합니다."

            ctx = {
                "form": form,
                "error_nickname_same": error_nickname_same,
                # "er" : form.non_field_errors(),
            }
            return render(request, "login/signup.html", ctx)
    # if request.method == "POST":
    #     form = SignUpForm(request.POST)
    #     if(request.POST.get("is_ToS")):
    #         # is_ToS 체크돼서 올때
    #         if form.is_valid():
    #             user = form.save()
    #             return redirect("login:signup_success")
    #         else:
    #             ctx = {
    #                 "form": form,
    #             }
    #             return render(request, "login/signup.html", ctx)
    #     else:
    #         # is_ToS 체크 안돼서 올때
    #         ctx = {
    #             "form": form,
    #             "ToS_error": "약관에 동의해야합니다."
    #         }
    #         return render(request, "login/signup.html", ctx)
    elif request.method == "GET":
        form = SignUpForm()
        ctx = {
            "form": form,
        }
        return render(request, "login/signup.html", ctx)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("login:login_success")
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
        return redirect("home")
    elif request.method == "GET":
        return redirect("login:logout_success")


def signup_success(request):
    return render(request, "login/signup_success.html")

def login_success(request):
    return render(request, "login/login_success.html")

def logout_success(request):
    return render(request, "login/logout_success.html")


@allowed_users
def my_page(request):
    me = request.user
    friends = me.friend_set.all().filter(accepted=True)
    # me = get_object_or_404(User, id=pk) #me = 접속한 user
    # friends = me.self_set.all() #me의 friend들
    friends_enrollment = {}
    motivation_from_friends = me.motivation_friend_set.all()

    for friend in friends:
        friends_enrollment[friend.me.id] = EnrollmentDate.objects.all().filter(enrollment__player=friend.me, date_result=True).count()

    today = date.today() #오늘 날짜에 맞는 챌린지만 가져오게 하기
    enrollmentdates = EnrollmentDate.objects.all().filter(
            enrollment__player=me, date__year=today.year, date__month=today.month, date__day=today.day)
    challenge_success = EnrollmentDate.objects.all().filter(
            enrollment__player=me, date_result=True)#.order_by('-pk')
    
    challenge_success_title = {}
    for ch in challenge_success:
        challenge_success_title[ch.enrollment.pk] = ch.enrollment.challenge.title
    
    challenge_success_serializer = json.Serializer()
    challenge_success_serialized = challenge_success_serializer.serialize(
        challenge_success)
    ctx = {        
        'me': me,
        'friends': friends,
        'enrollmentdates': enrollmentdates,
        'friends_enrollment': friends_enrollment,
        'motivation_from_friends': motivation_from_friends,
        'challenge_success' : JSON.dumps(challenge_success_serialized),
        'challenge_success_title' : JSON.dumps(challenge_success_title),
    }

    print(ctx)
    return render(request, "login/mypage.html", ctx)


@csrf_exempt
def result_ajax(request):
    req = JSON.loads(request.body)
    enrollmentdate = EnrollmentDate.objects.get(id=req["id"])
    enrollment_title = enrollmentdate.enrollment.challenge.title
    if enrollmentdate.date_result == False:
        enrollmentdate.date_result = True
    else:
        enrollmentdate.date_result = False
    enrollmentdate.save()

    return JsonResponse({'id': enrollmentdate.id, 'result': enrollmentdate.date_result, 'title': enrollment_title})



# settings

@required_login
@allowed_users
def settings_main(request):
    return render(request, "login/settings_main.html")


# Forbidden (CSRF token missing or incorrect.) 문제로 데코레이터 추가함
@csrf_exempt
def userinfo_get(request):
    user_name = request.user.username
    user_nickname = request.user.nickname
    user_email = request.user.email
    user_is_social = request.user.is_social
    user_image = request.user.image.url
    print(user_image)
    return JsonResponse({"name": user_name, "nickname": user_nickname, "email": user_email, "is_social": user_is_social, "image": user_image})


# # challenge 자체의 모든 내용들을 보내는 방식
# @csrf_exempt
# def userchallenge_get(request):
#     user = request.user
#     user_enrollment_list = user.chEnrollment_set.all()  # user의 enrollment list
#     user_challenge_list = []    # user가 참여한 challenge list

#     # enrollment list 직렬화 --> QuerySet을 json으로 변환
#     enrollment_list_serializer = json.Serializer()
#     enrollment_list_serialized = enrollment_list_serializer.serialize(
#         user_enrollment_list)

#     # user가 참여한 challenge를 user_enrollment_list를 통해 가져와 list로 담음
#     for i, ch in enumerate(list(user_enrollment_list)):
#         user_challenge_list.append(ch.challenge)

#     # challenge list 직렬화 --> QuerySet을 json으로 변환
#     challenge_list_serializer = json.Serializer()
#     challenge_list_serialized = challenge_list_serializer.serialize(
#         user_challenge_list)

#     return JsonResponse({"enrollment_list": enrollment_list_serialized, "challenge_list": challenge_list_serialized})


# challenge에서 필요한 내용들만 보내는 방식
@csrf_exempt
def userchallenge_get(request):
    user = request.user
    user_enrollment_list = user.chEnrollment_set.all()  # user의 enrollment list
    user_challenge_list = []    # user가 참여한 challenge list

    # user가 참여한 challenge를 user_enrollment_list를 통해 가져와 list로 담음
    for i, ch in enumerate(list(user_enrollment_list)):
        user_challenge_list.append({"invitation_key" : ch.challenge.invitation_key, "title" : ch.challenge.title, "status" : ch.challenge.status})

    return JsonResponse({"challenge_list": user_challenge_list})



@csrf_exempt
def usersetting_get(request):
    # 설정사항들 정하고 모델에 필드 추가하기
    return JsonResponse({})


# settings 2차
def userinfo_modify(request):
    if request.method == "POST":
        form = UserInfoModifyForm(request.POST, instance=request.user)
        image_form = UserImageModifyForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid() and image_form.is_valid():
            form.save()
            image_form.save()
            return redirect("login:settings")
        else:
            error_nickname_same = ""

            if form.non_field_errors():
                error_nickname_same = "사용자의 닉네임은/는 이미 존재합니다."

            ctx = {
                "form": form,
                "image_form": image_form,
                "error_nickname_same": error_nickname_same,
            }
            return render(request, "login/userinfo_modify.html", ctx)
    elif request.method == "GET":
        form = UserInfoModifyForm(instance=request.user)
        image_form = UserImageModifyForm(instance=request.user)
        ctx = {
            "form": form,
            "image_form": image_form,
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


def social_sign_up(request):
    if request.method == "POST":
        form = SocialSignUpForm(request.POST, instance=request.user)
        if form.is_valid():
            request.user.is_social = True
            # TODO : 만약 로컬 회원가입 시 is_ToS 등이 false일 경우 로컬 계정은 소셜 계정이 됨
            user = form.save()
            return redirect("login:signup_success")
        else:
            error_nickname_same = ""

            if form.non_field_errors():
                error_nickname_same = "사용자의 닉네임은/는 이미 존재합니다."

            ctx = {
                "form": form,
                "error_nickname_same": error_nickname_same,
                # "er" : form.non_field_errors(),
            }
            return render(request, "login/social_signup.html", ctx)

    # if request.method == "POST":
    #     form = SocialSignUpForm(request.POST, instance=request.user)
    #     if(request.POST.get("is_ToS")):
    #         # is_ToS 체크돼서 올때
    #         if form.is_valid():
    #             request.user.is_social = True
    #             # TODO : 만약 로컬 회원가입 시 is_ToS 등이 false일 경우 로컬 계정은 소셜 계정이 됨
    #             user = form.save()
    #             return redirect("login:signup_success")
    #         else:
    #             ctx = {
    #                 "form": form,
    #             }
    #             return render(request, "login/social_signup.html", ctx)
    #     else:
    #         # is_ToS 체크 안돼서 올때
    #         ctx = {
    #             "form": form,
    #             "ToS_error": "약관을 동의해야합니다."
    #         }
    #         return render(request, "login/social_signup.html", ctx)
    elif request.method == "GET" and (request.user.is_ToS == False or request.user.email == None or request.user.username == None or request.user.nickname == None):
        form = SocialSignUpForm(instance=request.user)
        ctx = {
            "form": form,
        }
        return render(request, "login/social_signup.html", ctx)

    elif request.method == "GET":
        return redirect("login:login_success")