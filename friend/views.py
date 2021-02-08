from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Friendship
from challenge.models import Challenge, Enrollment
from login.models import User
from .forms import FriendshipForm
from django.views.generic import CreateView, UpdateView

# Create your views here.

def fd_list(request):
    me = request.user
    friends = me.friend_set.all().filter(accepted=True)
    friends_pending = me.friend_set.all().filter(accepted=False)

    ctx = {        
        'me': me,
        'friends': friends,
        'pendings' : friends_pending,
    }
    return render(request, 'friend/friend_list.html', context=ctx)

# def fd_create(request, pk):
#     # idea_new = CreateView.as_view(model=Idea, form_class=IdeaForm, template_name_suffix = '_create')

#fd_create = CreateView.as_view(model=Friendship, form_class=FriendshipForm, template_name_suffix="_create")

def fd_create(request):
    user = request.user
    if request.method == "POST":
        form = FriendshipForm(request.POST)
        if form.is_valid():
            connection = form.save()
            connection.me = user

            #이부분 최적화가 가능하다면 이후에 할 필요 있음
            # form.save된 과정에서 이미 존재하는 쿼리의 경우 unique set을 삭제해줘야하는 이슈 발생 -> 수정은 완료
            if Friendship.objects.filter(me=connection.me, friend=connection.friend).exists():
                connection.delete()
                return redirect('friend:fd_list')
            else:
                connection = form.save()
                return redirect('friend:fd_list')

                # #반대의 관계도 생성
                # opposite = Friendship.objects.create(
                #     me = connection.friend,
                #     friend = connection.me
                # )

                # return redirect('friend:fd_list')

    else:
        form = FriendshipForm()
        ctx = {
            'form': form
        }
        return render(request, "friend/friend_create.html", context=ctx)


def fd_approve(request, pk):
    if request.method == "POST":
        target = User.objects.get(id=pk)
        friendship = Friendship.objects.get(me=target, friend=request.user)
        friendship.accepted = True
        friendship.save()

        opposite = Friendship.objects.create(
            me = friendship.friend,
            friend = friendship.me,
            accepted = True,
        )

        return redirect('friend:fd_list')
    else:
        return redirect('friend:fd_list')

def fd_deny(request, pk):
    if request.method == "POST":
        target = User.objects.get(id=pk)
        friendship = Friendship.objects.get(me=target, friend=request.user)
        friendship.delete()

        return redirect('friend:fd_list')
    else:
        return redirect('friend:fd_list')


def fd_detail(request, pk):
    user = User.objects.get(pk=pk)
    enrollments = Enrollment.objects.all().filter(player=user)
    #challenges = user.player_set.all()
    ctx = {
        'user': user,
        'enrollments': enrollments,
    }
    return render(request, 'friend/friend_detail.html', context=ctx)


def fd_delete(request, pk):
    me = request.user
    friend = get_object_or_404(User, id=pk)

    if request.method == "GET":
        return redirect('friend:fd_detail', friend.id)
    elif request.method == "POST":
        friendship = get_object_or_404(Friendship, me=me, friend=friend)
        friendship.delete()
        friendship = get_object_or_404(Friendship, me=friend, friend=me)
        friendship.delete()
        return redirect('friend:fd_list')
