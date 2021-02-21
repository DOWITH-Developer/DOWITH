from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Q    
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ChallengeForm, SearchForm
from django.views.generic import FormView
import datetime
# ajax
from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import date
import threading
import time
import hashlib
# decorator
from login.decorators import allowed_users
from django.contrib.auth.decorators import login_required
# dic
from django.template.defaultfilters import register


#TODO challenge_detail view Ajax 변수명 수정


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def home(request):
    return render(request, "challenge/home.html")

def challenge_list(request):
    alls = Challenge.objects.filter(private=0,status=0)
    languages = Challenge.objects.filter(
        category=Challenge.CATEGORY_LANGUAGE,private=0,status=0)
    jobs = Challenge.objects.filter(
        category=Challenge.CATEGORY_JOB,private=0,status=0)
    NCSs = Challenge.objects.filter(
        category=Challenge.CATEGORY_NCS,private=0,status=0)
    programmings = Challenge.objects.filter(
        category=Challenge.CATEGORY_PROGRAMMING,private=0,status=0)
    certificates = Challenge.objects.filter(
        category=Challenge.CATEGORY_CERTIFICATE,private=0,status=0)
    others = Challenge.objects.filter(
        category=Challenge.CATEGORY_OTHER,private=0,status=0)
        
    if request.method == 'GET':
        form = SearchForm()
        ctx = {
            'alls': alls,
            'languages': languages,
            'jobs': jobs,
            'NCSs': NCSs,
            'programmings': programmings,
            'certificates': certificates,
            'others': others,
            'form': form,
        }
        return render(request, 'challenge/challenge_list.html', ctx)

    else:
        form = SearchForm(request.POST)
        searchWord = request.POST["search_word"]
        ChallengeList = Challenge.objects.filter(Q(title__icontains=searchWord))
        # distinct() 함수는 중복 방지, 나중에 추가

        context = {
            'alls': alls,
            'languages': languages,
            'jobs': jobs,
            'NCSs': NCSs,
            'programmings': programmings,
            'certificates': certificates,
            'others': others,
            'form' : form,
            'search_term' : searchWord,
            'challenge_list' : ChallengeList
        }
        return render(request, 'challenge/challenge_list.html', context)


def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)

    if Enrollment.objects.filter(challenge=challenge, player=request.user).exists():
        status = True
        enrollment = Enrollment.objects.get(player=request.user, challenge=challenge)
    else:
        status = False
        enrollment = None

    data = {
        "challenge": challenge, 
        "status": status,
        "enrollment": enrollment,
        # "private": challenge.private
    }

    #TODO view 정리하기
    today = datetime.date.today()
    if challenge.start_date > today:
        challenge.status = 0
        challenge.save()
        return render(request, "challenge/challenge_detail.html", data)
    elif challenge.start_date <= today < challenge.end_date:
        # 진행상황 (진행중)
        challenge.status = 1
        challenge.save()
        return render(request, "challenge/challenge_ing.html", data)
    else:
        challenge.status = 2
        challenge.save()
        return render(request, "challenge/challenge_done.html", data)


@login_required
@allowed_users
def challenge_enrollment(request, pk):
    if request.method == "POST":  
        player = request.user
        challenge = Challenge.objects.get(pk=pk)
        challenge.cur_pp += 1
        challenge.save()

        enrollment = Enrollment.objects.create(
            player = player, 
            challenge = challenge,
            )
        return redirect(f'/challenge/list/{challenge.pk}')
    else:
        return redirect(f'/challenge/list/{challenge.pk}')


@login_required
@allowed_users
def challenge_create(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST, request.FILES)
        
        if form.is_valid():
            challenge = form.save()
            challenge.status = 0

            #url hash 값 생성
            HASH_NAME = "md5"
            temp_hash = str(challenge.pk)

            text = temp_hash.encode('utf-8')
            md5 = hashlib.new(HASH_NAME)
            md5.update(text)
            result = md5.hexdigest()

            challenge.invitation_key = result

            #create 와 동시에 enrollment 로 할당
            Enrollment.objects.create(
                player=request.user,
                challenge=challenge
            )
            challenge.cur_pp += 1
            challenge.save()

            return redirect(f'/challenge/list/{challenge.pk}')
        else:
            # error_list 딕셔너리로 넘겨주지않고, 각각 변수로 넘겨줄때
            # error_pp = ""
            # error_date = ""
            # error_category = ""
            # error_private = ""
            error_list = {}
            # print(request.POST.get("category"))
            # print(request.POST.get("private"))

            if request.POST.get("category") == None:
                # error_category = "카테고리를 선택해야 합니다."
                error_list["category"] = "카테고리를 선택해야 합니다."
            if request.POST.get("private") == None:
                # error_private = "공개 상태를 선택해야 합니다."
                error_list["private"] = "공개 상태를 선택해야 합니다."

            for error in form.non_field_errors():
                if error == "최대 인원이 최소 인원보다 작을 수 없습니다.":
                    # error_pp = error
                    error_list["pp"] = "최대 인원이 최소 인원보다 작을 수 없습니다."
                elif error == "종료일이 시작일보다 빠를 수 없습니다.":
                    # error_date = error
                    error_list["date"] = "종료일이 시작일보다 빠를 수 없습니다."
            
            ctx = {
                "form": form,
                # "error_pp" : error_pp,
                # "error_date" : error_date,
                # "error_category" : error_category,
                # "error_private" : error_private,
                "error_list" : error_list,
            }
            return render(request, "challenge/challenge_create.html", ctx)
    else:
        form = ChallengeForm()
    return render(request, 'challenge/challenge_create.html', {"form": form})

def challenge_delete(request, pk):
    if request.method == "POST":
        player = request.user
        challenge = Challenge.objects.get(pk=pk)
        challenge.cur_pp -= 1
        challenge.save()
        enrollment = get_object_or_404(Enrollment, player=player, challenge=challenge)
        enrollment.delete()
        return redirect(f'/challenge/list/{challenge.pk}')
    else: #GET
        return redirect(f'/challenge/list/{challenge.pk}')


    return redirect(f'/challenge/list/{challenge.pk}')

#날짜바뀔때 실행하는 EnrollmentDate객체 만드는 함수
# def make_enrollment_date():
#     for E in Enrollment.objects.all().filter(status=1):
#         new_ed = EnrollmentDate(enrollment=E)
#         new_ed.save() #오늘의 날짜로 EnrollmentDate 생성

def challenge_calendar(request):
    return render(request, 'challenge/challenge_calendar.html')


class ResultAjax(View):
    # 포비든 문제때문에 추가
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ResultAjax, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        req = json.loads(request.body)
        challenge_id = req["id"]
        challenge = Challenge.objects.get(id=challenge_id)
        enrollment = Enrollment.objects.get(player=request.user, challenge=challenge)
        print(enrollment.result)

        if enrollment.result == False:
            enrollment.result = True
        else:
            enrollment.result = False
        enrollment.save()

        return JsonResponse({'id': challenge_id, 'result': enrollment.result})

#         if challenge.success.filter(id=user.id).exists():
#             # user has already liked this company
#             # remove like/user
#             challenge.success.remove(user)
#             message = 'You disliked this'
#         else:
#             # add a new like for a company
#             challenge.success.add(user)
#             message = 'You liked this'

#     ctx = {'likes_count': challenge.total_likes, 'message': message}
#     # use mimetype instead of content_type if django < 5
#     return HttpResponse(json.dumps(ctx), content_type='application/json')


def challenge_invitation(request, invitation):
    challenge = Challenge.objects.get(invitation_key=invitation)
    
    if Enrollment.objects.filter(challenge=challenge, player=request.user).exists():
        status = True
        enrollment = Enrollment.objects.get(player=request.user, challenge=challenge)
    else:
        status = False
        enrollment = None

    data = {
        "challenge": challenge, 
        "status": status,
        "enrollment": enrollment,
        # "private": challenge.private
    }
    # print(enrollment.total_player())
    # print(data)    
    return render(request, "challenge/challenge_detail.html", data) 



class InvitationAjax(View):
    # 포비든 문제때문에 추가
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(InvitationAjax, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        req = json.loads(request.body)
        challenge_id = req["id"]
        print(challenge_id)
        challenge = Challenge.objects.get(id=challenge_id)

        return JsonResponse({'id': challenge_id, 'invitation_key': challenge.invitation_key})

def invitation_accept(request):
    if request.method == 'POST':
        invitation_key = request.POST['invitation_key']

        if Challenge.objects.filter(invitation_key=invitation_key).exists():
            return redirect(f'/challenge/invite/' + invitation_key)
        else:
            return redirect(f'/challenge/invitation/failed')
    else:    
        return render(request, 'challenge/invitation_accept.html')

def invitation_failed(request):
    return render(request, 'challenge/invitation_failed.html')


class SearchAjax(View):
    # 포비든 문제때문에 추가
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SearchAjax, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        req = json.loads(request.body)
        word = req["value"]
        # friendship 인스턴스 중 me field 가 user 인 인스턴스만 접근하는 방식
        user = request.user
        challenge_list = [] # user 의 친구 list
        
        challenge = user.self_set.filter(Q(challenge__title__icontains=word))
        challenge_serializer = JSON.Serializer()
        challenge_serialized = challenge_serializer.serialize(challenge)
        
        # friend 를 serialize 해서 json 으로 넘겨줬는데, 이게 끝이 아니라 friend list 를 넘겨줘야해
        
        for i, ch in enumerate(list(challenge)):
            challenge_list.append(ch.title)
        
        challenge_list_serializer = JSON.Serializer()
        challenge_list_serialized = challenge_list_serializer.serialize(challenge_list)
    
        return JsonResponse({"challenge" : challenge_serialized, "challenge_list" : challenge_list_serialized})
     