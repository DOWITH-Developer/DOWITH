from django.db import models
from login.models import User

# Create your models here.
class Friendship(models.Model):
    me = models.ForeignKey(User, on_delete=models.CASCADE, related_name='self_set', blank=True, null=True)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend_set")

