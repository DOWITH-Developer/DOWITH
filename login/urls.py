from django.urls import path, include
from .views import *

app_name = 'login'

urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("layout/", test, name="test"),  # 테스트용
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("<int:pk>/mypage/",my_page, name="my_page"),
    # settings
    path("settings/", settings_main, name="settings"),
    path("settings/user_info/", userinfo_get, name="user_info"),
    path("settings/user_challenge/", userchallenge_get, name="user_challenge"),
    path("settings/setting/", usersetting_get, name="user_setting"),
    # settings 2차
    path("userinfo_modify/", userinfo_modify, name="userinfo_modify"),
    path("userinfo_password_modify/", userinfo_password_modify,
         name="userpassword_modify"),
]
