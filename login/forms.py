from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["is_ToS", "email", "username", "nickname"]

    # def clean(self):
    #     form_data = self.cleaned_data
    #     username = self.cleaned_data.get("username")
    #     nickname = self.cleaned_data.get("nickname")
    #     is_ToS = self.cleaned_data.get("is_ToS")

    #     if username == nickname and is_ToS == False:
    #         raise forms.ValidationError("둘이 같으면 안돼 / 안돼안돼")
    #     elif username == nickname:
    #         raise forms.ValidationError("둘이 같으면 안돼")
    #     elif is_ToS == False:
    #         raise forms.ValidationError("안돼안돼")
    #     # return form_data
    

    # def clean_username(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")
    #     print(username)
    #     if username == "안녕":
    #         raise forms.ValidationError("안녕은 안돼")
    #     return username

    # def clean_is_ToS(self, *args, **kwargs):
    #     is_ToS = self.cleaned_data.get("is_ToS")
    #     print(is_ToS)
    #     if is_ToS == False:
    #         raise forms.ValidationError("약관에 동의해야 합니다.")
    #     return is_ToS

# class SocialSignUpForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     nickname = forms.CharField(max_length=100)

#     def signup(self, request, user):
#         user.username = self.cleaned_data["username"]
#         user.nickname = self.cleaned_data["nickname"]
#         user.is_social = True
#         # user.username = self.cleaned_data["last_name"] + \
#         #     self.cleaned_data["first_name"]
#         # user.nickname = self.cleaned_data["last_name"] + \
#         #     self.cleaned_data["first_name"]
#         user.save()

class SocialSignUpForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["is_ToS", "email", "username", "nickname"]


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {"password": forms.PasswordInput}


class UserInfoModifyForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["username", "nickname"]


class UserImageModifyForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["image"]


class UserPasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = User
        field = "__all__"
