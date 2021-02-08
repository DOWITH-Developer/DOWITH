from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "nickname", "email"]


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {"password": forms.PasswordInput}


class UserInfoModifyForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["username", "nickname", "email", "password"]


class UserPasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = User
        field = "__all__"
