from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django import forms
# Create your models here.
from django.core.exceptions import ValidationError

def is_ToS(value):
    if value == False:
        raise forms.ValidationError("약관에 동의해야 합니다.")
 
class User(AbstractUser):
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=150)
    image = models.ImageField(upload_to="profile_photo/%Y/%m/%d/", default="profile_photo/default/DOWITH.png")
    is_social = models.BooleanField(default=False)
    is_ToS = models.BooleanField(default=False, validators=[is_ToS])

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "nickname"]

    def __str__(self):
        return str(self.nickname)

    # # def clean_fields(self, *args, **kwargs):
    # #     username = self.username
    # #     nickname = self.nickname
    # #     print(username)
    # #     if username == nickname:
    # #         raise ValidationError("둘이 같으면 안돼")
    # #     return super(User, self).clean_fields(*args, **kwargs)
    
    # # def clean_fields(self, *args, **kwargs):
    # #     if self.is_ToS == False:
    # #         raise ValidationError("안돼안돼")
    # #     return super(User, self).clean_fields(*args, **kwargs)
    
    # def clean(self, *args, **kwargs):
    #     if self.is_ToS == False:
    #         raise ValidationError("안돼안돼")
    #     return super(User, self).clean(*args, **kwargs)

    # def clean(self, *args, **kwargs):
    #     if self.username == self.nickname and self.is_ToS == False:
    #         raise ValidationError("둘이 같으면 안돼 / 안돼안돼")
    #     elif self.username == self.nickname:
    #         raise ValidationError("둘이 같으면 안돼")
    #     elif self.is_ToS == False:
    #         raise ValidationError("안돼안돼")
    #     return super(User, self).clean(*args, **kwargs)
    

    # # def clean_is_ToS(self, *args, **kwargs):
    # #     is_ToS = self.cleaned_data.get("is_ToS")
    # #     print(is_ToS)
    # #     if is_ToS == False:
    # #         raise forms.ValidationError("약관에 동의해야 합니다.")
    # #     return is_ToS