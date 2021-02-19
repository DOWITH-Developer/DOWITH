from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Friendship, Motivation
from challenge.models import Challenge, Enrollment
from django.db.models import Q
from login.models import User
from .forms import FriendshipForm, FriendSearchForm
from django.views.generic import CreateView, UpdateView
from django.views import View
import json
from challenge.models import *  # Enrollment가져옴
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.core.serializers import json as JSON

# Create your views here.

def fd_list(request):
    
    me = request.user
    friends = me.friend_set.all().filter(accepted=True)
    friends_pending = me.friend_set.all().filter(accepted=False)
    #motivation을 위한 코드
    motivation_from_friends = me.motivation_friend_set.all()

    if request.method == 'GET':
        form = FriendSearchForm()
        ctx = {        
            'friends': friends,
            'pendings' : friends_pending,
            'form': form,

            #motivation을 위한 코드
            'motivation_from_friends' : motivation_from_friends,
        }
        return render(request, 'friend/friend_list.html', context=ctx)

    # else:
        # form = FriendSearchForm(request.POST)
        # searchWord = request.POST["search_word"]
        # #! 왜 me.friend_set 으로 접근하는지
        # friends = me.friend_set.filter(Q(me__nickname__icontains=searchWord))
        # ctx = {        
        #     'friends': friends,
        #     'pendings' : friends_pending,
        #     'form': form,

        #     #motivation을 위한 코드
        #     'motivation_from_friends' : motivation_from_friends,
        # }
        # return render(request, 'friend/friend_list.html', context=ctx)

def fd_create(request):
    return render(request, 'friend/friend_create.html')


def new_fd_create(request, pk):
    user = request.user
    friend = User.objects.get(id=pk)
    
    if request.method == "POST":
        form = FriendshipForm(request.POST)
        if form.is_valid():
            connection = form.save()
            connection.me = user
            connection.friend = friend

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
        return redirect('friend:fd_list')


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


#TODO 대시보드에서 수정사항 있을 수 있음 -> 지금 바꾸기 때문
def fd_detail(request, pk):
    me = request.user
    user = User.objects.get(pk=pk)
    enrollments = Enrollment.objects.all().filter(player=user)

    #만약 detail을 조회한 사람이 친구관계에 있는 사람이 아니라면
    friendship = Friendship.objects.filter(me=me, friend=user, accepted=True).exists()
    #challenges = user.player_set.all()
    ctx = {
        'user': user,
        'enrollments': enrollments,
        'friendship': friendship,
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

def fd_more(request,pk):
    me = get_object_or_404(User, id=pk) #me = 접속한 user
    friends = me.self_set.all() #me의 friend들
    ctx = {        
        'me': me,
        'friends': friends,
    }
    return render(request, "friend/friend_more.html", ctx)


class MotivationAjax(View):
    # 포비든 문제때문에 추가
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MotivationAjax, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        req = json.loads(request.body)
        user_id =req['id']
        user = User.objects.get(id=user_id)

        if not(Motivation.objects.filter(me=request.user, friend=user).exists()):
            motivation = Motivation.objects.create(
                me=request.user,
                friend=user
        )
        else:
            motivation = Motivation.objects.get(me=request.user, friend=user)
            motivation.count += 1
            motivation.save()
        return JsonResponse({'user': user.nickname, 'count':motivation.count})

class MotivationRemoveAjax(View):
    # 포비든 문제때문에 추가
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MotivationRemoveAjax, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        req = json.loads(request.body)

        #모두 지우기 일 경우
        if req['id'] == None:
            me = request.user
            motivations = Motivation.objects.all().filter(friend=me)
            
            for motivation in motivations:
                motivation.delete()
            
            return JsonResponse({'status': True})
            

        #특정 콕 찌르기만 지우기일 경우
        else:
            motivation = Motivation.objects.get(id=req['id'])
            motivation.delete()

            return JsonResponse({'id': motivation.id})
        
    
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
        friend_list = [] # user 의 친구 list
        
        friend = user.self_set.filter(Q(friend__nickname__icontains=word))
        friend_serializer = JSON.Serializer()
        friend_serialized = friend_serializer.serialize(friend)
        
        # friend 를 serialize 해서 json 으로 넘겨줬는데, 이게 끝이 아니라 friend list 를 넘겨줘야해
        
        for i, ch in enumerate(list(friend)):
            friend_list.append(ch.friend)

        friend_list_serializer = JSON.Serializer()
        friend_list_serialized = friend_list_serializer.serialize(friend_list)
    
        return JsonResponse({"friend" : friend_serialized, "friend_list" : friend_list_serialized})
        
        # if request.method == 'GET':
        # form = FriendSearchForm()
        # ctx = {        
        #     'friends': friends,
        #     'pendings' : friends_pending,
        #     'form': form,
        #     'motivation_from_friends' : motivation_from_friends,
        # }   


class SearchUserAjax(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SearchUserAjax, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        me = request.user
        req = json.loads(request.body)
        word = req['value']
        if word == "":
            return JsonResponse({'user_list': None})
        else:
            users = User.objects.all().filter().exclude(email=request.user.email)
            users = users.filter(Q(nickname__icontains=word))
        
            user_list = {}

            for user in users:
                if not(Friendship.objects.filter(me=me, friend=user, accepted=True).exists()):
                    user_list[user.id] = {'pk':user.pk, 'username':user.username, 'nickname':user.nickname}
                    
                    #리스트로 할 경우
                    #user_list.append({'pk':user.pk, 'username':user.username, 'nickname':user.nickname})

            return JsonResponse({'user_list': user_list})
