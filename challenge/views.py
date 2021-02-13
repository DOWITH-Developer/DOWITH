from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ChallengeForm
# ajax
from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def ch_list(request):
    if request.method == 'GET':
        alls = Challenge.objects.all()
        languages = Challenge.objects.filter(
            category=Challenge.CATEGORY_LANGUAGE)
        jobs = Challenge.objects.filter(
            category=Challenge.CATEGORY_JOB)
        NCSs = Challenge.objects.filter(
            category=Challenge.CATEGORY_NCS)
        programmings = Challenge.objects.filter(
            category=Challenge.CATEGORY_PROGRAMMING)
        certificates = Challenge.objects.filter(
            category=Challenge.CATEGORY_CERTIFICATE)
        others = Challenge.objects.filter(
            category=Challenge.CATEGORY_OTHER)
        ctx = {
            'alls': alls,
            'languages': languages,
            'jobs': jobs,
            'NCSs': NCSs,
            'programmings': programmings,
            'certificates': certificates,
            'others': others,
        }
        return render(request, 'challenge/ch_list.html', ctx)
    else:
        pass


def challenge_detail(request, pk):
    challenge = Challenge.objects.get(pk=pk)
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


def challenge_enrollment(request, pk):
    if request.method == "POST":  
        player = request.user
        challenge = Challenge.objects.get(pk=pk)

        enrollment = Enrollment.objects.create(
            player = player, 
            challenge = challenge,
            )
        return redirect(f'/challenge/{challenge.pk}')
    else: 
        return redirect(f'/challenge/{challenge.pk}')


def challenge_create(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST, request.FILES)
        if form.is_valid():
            challenge = form.save()
            return redirect(f'/challenge/{challenge.pk}')
    else:
        form = ChallengeForm()
    return render(request, 'challenge/challenge_create.html', {"form": form})


def challenge_delete(request, pk):
    if request.method == "POST":
        player = request.user
        challenge = Challenge.objects.get(pk=pk)
        enrollment = get_object_or_404(Enrollment, player=player, challenge=challenge)
        enrollment.delete()
        return redirect('/challenge/list/')
    else: #GET
        return redirect('/challenge/list/')


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
