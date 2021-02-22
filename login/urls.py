from django.urls import path, include
from .views import *

app_name = 'login'

urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("mypage/",my_page, name="my_page"),
    # settings
    path("settings/", settings_main, name="settings"),
    path("settings/user_info/", userinfo_get, name="user_info"),
    path("settings/user_challenge/", userchallenge_get, name="user_challenge"),
    path("settings/setting/", usersetting_get, name="user_setting"),
    # settings 2차
    path("userinfo_modify/", userinfo_modify, name="userinfo_modify"),
    path("userinfo_password_modify/", userinfo_password_modify,
         name="userinfo_password_modify"),
    # social sign up
    path("social_signup/", social_sign_up, name="social_signup"),
    # success
    path("signup_success/", signup_success, name='signup_success'),
    path("login_success/", login_success, name="login_success"),
    path("logout_success/", logout_success, name="logout_success"),
]
