from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django import forms
# Create your models here.

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
