from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User
from django import forms

# from allauth.socialaccount.forms import SignupForm
# from allauth.account.forms import SignupForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "nickname", "email", "first_name"]


class SS(forms.Form):
    username = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=100)
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)

    # 필요한건가?
    # class Meta:
    #     model = User

    def signup(self, request, user):
        user.username = self.cleaned_data["username"]
        user.nickname = self.cleaned_data["nickname"]
        # user.username = self.cleaned_data["last_name"] + \
        #     self.cleaned_data["first_name"]
        # user.nickname = self.cleaned_data["last_name"] + \
        #     self.cleaned_data["first_name"]
        user.save()


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {"password": forms.PasswordInput}


class UserInfoModifyForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["username", "nickname"]


class UserPasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = User
        field = "__all__"
