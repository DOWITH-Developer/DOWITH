import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from challenge.models import *
import datetime

#날짜바뀔때 실행하는 EnrollmentDate객체 만드는 함수

def change_challenge_status():
    today = datetime.date.today()
    for C in Challenge.objects.all():
        if C.start_date > today:
            C.status = 0
            C.save()
        elif C.end_date < today:
            C.status = 2
            C.save()
        else:
            C.status = 1
            C.save()


def make_enrollment_date():
    for E in Enrollment.objects.all().filter(challenge__status=1):
        if not(EnrollmentDate.objects.filter(enrollment=E, date=datetime.date.today()).exists()):
            new_ed = EnrollmentDate(enrollment=E, date=datetime.date.today())
            new_ed.save() #오늘의 날짜로 EnrollmentDate 생성


#12시에 시작 하면 안돼 큰일남
#1. 지현이가 한 것 -> 12시가 되면 오늘과 스타트 데이트를 비교해서 status 정보를 바꿔줘야 함
#2. 바뀐 status정보를 가지고 오늘을 기점으로 status가 1인 enrollment들만 enrollmentDate로 새로 만들어 줘야해


change_challenge_status()
make_enrollment_date()
