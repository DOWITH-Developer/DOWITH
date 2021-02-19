from django.db import models
from login.models import User

# Create your models here.
class Friendship(models.Model):
    me = models.ForeignKey(User, on_delete=models.CASCADE, related_name='self_set', blank=True, null=True)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend_set", blank=True, null=True)
    accepted = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('me', 'friend',)

class Motivation(models.Model):
    me = models.ForeignKey(User, on_delete=models.CASCADE, related_name="motivation_me_set")
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="motivation_friend_set")
    count = models.PositiveIntegerField(default=1)



# (A, B) / (B, A) = 동일

# fs

# fs1.me = fs2.friend
# fs2.me = fs1.friend


# fs = FriendShip()


# fs.save()


# -----------------------------
# 우아한 방법
# pre_save() <-- 생성되기 직전에 하는 액션; 만약에 me / friend 순서 바뀐게 있으면, 저장하지 마세요!
# save() <-- DB에 들어감
# post_save() <-- 생성된 후에 하는 액션


# 친구 요청 / 수락
# 요청 pre_save()
# 수락 -> save()
# 상대방과의 opposite connection post_save()


# -------------------------------
# fs = FriendShip(me=a, friend=b)
# fs2 = FriendShip(me=b, friend=a)
# fs.save()
# fs2.save()
