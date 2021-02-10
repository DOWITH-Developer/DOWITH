from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "nickname", "email", "first_name"]


class SS(forms.Form):
    # nickname = forms.CharField(max_length=100)
    # username = forms.CharField(max_length=100)
    # email = forms.EmailField(max_length=100)

    class Meta:
        model = User

    def signup(self, request, user):
        # user = super(SS, self).save(request)
        user.username = user.cleaned_data["name"]
        user.nickname = user.cleaned_data["name"]
        user.email = self.cleaned_data["email"]
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
