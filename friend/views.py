from django.shortcuts import render, HttpResponse
from .models import Friendship

# Create your views here.

def fd_list(request, pk):
    friends = Friendship.objects.filter(id=pk)
    ctx = {
        'friends': friends
    }
    return render(request, 'friend/friend_list.html', context=ctx)
    

def fd_create(request, pk):
    return HttpResponse('hello')

def fd_detail(request, pk):
    return HttpResponse('hello')

def fd_approve(request):
    return HttpResponse('hello')