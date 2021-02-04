from django.urls import path, include
from .views import *

app_name = 'login'

urlpatterns = [
    path("signup/", signUp, name="signup"),
    path("layout/", test, name="test"),
]
