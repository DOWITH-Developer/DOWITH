from django.urls import path, include
from .views import *

app_name = 'login'

urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("layout/", test, name="test"),  # 테스트용
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]
