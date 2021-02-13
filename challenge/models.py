from django.db import models
from login.models import User

# User
# - is staff : 내부자냐 아니냐

# Challenge
# - HostUser : user_id
# - is_published : Boolean
# - link_url : /challenge/cr23ou89hnacefijlnsho
# python hash
# URLSAFE : 띄어쓰기, 덧셈이 urlsafe functionå


def redirect_link(link):
    challenges = Challenge.objects.filter(link=link)
    if len(challenges) == 0:
        return
    else:
        pass
    return

# User <-> Challenge
# --> Enrollment
#      - user_id (User)
#      - challenge_id (Challenge)
#      - result/success
#      - day

# 이미지 저장
# 1. 파일 : Django File Upload
# 2. 외부 클라우드 스토리지 : 서버에서는 사진을 클라우드로 올리고, 클라우드 링크만 갖고있어요
# AWS S3, Microsoft, etc.


class Challenge(models.Model):
    CATEGORY_LANGUAGE = 'language'
    CATEGORY_JOB = 'job'
    CATEGORY_NCS = 'NCS'
    CATEGORY_PROGRAMMING = 'programming'
    CATEGORY_CERTIFICATE = 'certificate'
    CATEGORY_OTHER = 'other'

    CATEGORY_OF_CHALLENGE = (
        (CATEGORY_LANGUAGE, '어학'),
        (CATEGORY_JOB, '취업'),
        (CATEGORY_NCS, '고시/공무원'),
        (CATEGORY_PROGRAMMING, '프로그래밍'),
        (CATEGORY_CERTIFICATE, '자격증'),
        (CATEGORY_OTHER, '기타')
    )

    PRIVATE_OF_CHALLENGE = (
        (0, '전체 공개'),
        (1, '친구 공개'),
        (2, '나만 보기'),
    )

    STATUS_OF_CHALLENGE = (
        (0, '대기 중'),
        (1, '진행 중'),
        (2, '완료'),
    )

    title = models.CharField(max_length=100, verbose_name="제목")
    desc = models.TextField(verbose_name="설명")
    category = models.CharField(
        max_length=100, choices=CATEGORY_OF_CHALLENGE, verbose_name="분류")
    private = models.IntegerField(
        choices=PRIVATE_OF_CHALLENGE, verbose_name="공개 상태")
    status = models.IntegerField(
        choices=STATUS_OF_CHALLENGE, verbose_name="진행 상태")
    min_pp = models.PositiveIntegerField(verbose_name="최소 인원")
    max_pp = models.PositiveIntegerField(verbose_name="최대 인원")
    duration = models.PositiveIntegerField(verbose_name="기간")
    start_date = models.DateField(verbose_name="시작일")
    created_date = models.DateField(auto_now_add=True, verbose_name="생성일")
    link_url = models.URLField(blank=True, null=True)

    def link_url_uuid():
        return uuid.uuid4().hex

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    challenge = models.ForeignKey(
        Challenge, on_delete=models.CASCADE, verbose_name="챌린지", related_name="chEnrollment_set")
    player = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="유저", related_name="chEnrollment_set")
    result = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
    	unique_together = ('challenge', 'player',)

    def __str__(self):
        return str(self.challenge) +' '+ str(self.player)

    def total_player(self):
        return self.player.count()
