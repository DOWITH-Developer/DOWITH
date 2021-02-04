from django.db import models
from login.models import User

# Create your models here.
class Friendship(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_set")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower_set")