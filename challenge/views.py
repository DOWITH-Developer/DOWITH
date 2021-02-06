from .models import Challenge
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ChallengeForm


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
    data = {
        "challenge": challenge
    }

    return render(request, "challenge/challenge_detail.html", data)


def challenge_create(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST, request.FILES)
        if form.is_valid():
            challenge = form.save()  # ModelForm에서 제공
            return redirect(f'/challenge/{challenge.pk}')

    else:
        form = ChallengeForm()
    return render(request, 'challenge/challenge_create.html', {"form": form})


def challenge_delete(request, pk):
    if request.method == "GET":
        return redirect('/challenge/')

    # POST
    challenge = Challenge.objects.get(id=pk)
    challenge.delete()

    return redirect('/challenge/')


# try:
#     from django.utils import simplejson as json
# except ImportError:
#     import json


# @login_required
# @require_POST
# 오늘 성공했는 지 안 성공 했는 지

# def success(request):
#     # 유저, 챌린지 1개
#     # ACTION : 성공했는 지 안했는 지

#     if request.method == 'POST':
#         user = request.user
#         challenge_id??
#         # slug = request.POST.get('slug', None)
#         # challenge = get_object_or_404(Challenge, slug=slug)
#         challenge = get_object_or_404(Challenge, id=challenge_id)

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
