from django.shortcuts import redirect
from django.http import HttpResponse


# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse("You are not authorized to view this page")
#         return wrapper_func
#     return decorator


# def allowed_users(func):
#     def wrapper(self, request, *args, **kwargs):
#         if request.user.is_ToS == True:
#             print("y")
#             func()
#         else:
#             print("no")
#         return wrapper

from functools import wraps

# 약관 동의한 유저(소셜 계정의 유저)만이 접근할 수 있도록 하는 데코레이터
# 약관에 동의하지 않았을 경우 '추가 정보 입력 및 약관 동의' 페이지로 이동시킴
def allowed_users(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_ToS == True:
            return function(request, *args, **kwargs)
        else:
            return redirect("login:social_signup")

    return wrap


# # local user는 회원가입 시 무조건 약관을 동의하게 되어있음
# # 단, login view.py의 social_sign_up 함수에만 사용 가능 (소셜 계정의 유저 또한 결국엔 약관을 동의하게 되기 때문)
# def local_users(function):
#     @wraps(function)
#     def wrap(request, *args, **kwargs):
#         if request.user.is_ToS == True:
#             return function(request, *args, **kwargs)
#         else:
#             return redirect("login:social_signup")

#     return wrap



# 로그인 안 한 유저가 로그인한 유저만 할 수 있는 행위를 할때 로그인 페이지로 이동시키게 하기
def required_login(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        user = getattr(request, "user")

        if user and user.is_authenticated:
            return function(request, *args, **kwargs)

        return redirect("login:login")
    return wrap