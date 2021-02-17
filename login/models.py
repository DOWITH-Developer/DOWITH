from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=150)
    is_social = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "nickname"]

    def __str__(self):
        return str(self.nickname) + " " + str(self.username)
