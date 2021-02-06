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
            category=Challenge.CATEGORY_OF_CHALLENGE[1][0])
        jobs = Challenge.objects.filter(
            category=Challenge.CATEGORY_OF_CHALLENGE[2][0])
        NCSs = Challenge.objects.filter(
            category=Challenge.CATEGORY_OF_CHALLENGE[3][0])
        programmings = Challenge.objects.filter(
            category=Challenge.CATEGORY_OF_CHALLENGE[4][0])
        certificates = Challenge.objects.filter(
            category=Challenge.CATEGORY_OF_CHALLENGE[5][0])
        others = Challenge.objects.filter(
            category=Challenge.CATEGORY_OF_CHALLENGE[6][0])
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


try:
    from django.utils import simplejson as json
except ImportError:
    import json


@login_required
@require_POST
def success(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        challenge = get_object_or_404(Challenge, slug=slug)

        if challenge.success.filter(id=user.id).exists():
            # user has already liked this company
            # remove like/user
            challenge.success.remove(user)
            message = 'You disliked this'
        else:
            # add a new like for a company
            challenge.success.add(user)
            message = 'You liked this'

    ctx = {'likes_count': challenge.total_likes, 'message': message}
    # use mimetype instead of content_type if django < 5
    return HttpResponse(json.dumps(ctx), content_type='application/json')
