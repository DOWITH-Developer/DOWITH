from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Friendship
from login.models import User
from .forms import FriendshipForm
from django.views.generic import CreateView, UpdateView

# Create your views here.

def fd_list(request, pk):
    me = get_object_or_404(User, id=pk)
    friends = me.self_set.all()

    ctx = {        
        'me': me,
        'friends': friends
    }
    return render(request, 'friend/friend_list.html', context=ctx)

# def fd_create(request, pk):
#     # idea_new = CreateView.as_view(model=Idea, form_class=IdeaForm, template_name_suffix = '_create')

#fd_create = CreateView.as_view(model=Friendship, form_class=FriendshipForm, template_name_suffix="_create")

def fd_create(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = FriendshipForm(request.POST)
        if form.is_valid():
            connection = form.save()
            connection.me = user
            connection = form.save()

            #반대의 관계도 생성
            opposite = Friendship.objects.create(
                me = connection.friend,
                friend = connection.me
            )

            return redirect('friend:fd_list', pk)

            
    else:
        form = FriendshipForm()
        ctx = {
            'form': form
        }
        return render(request, "friend/friend_create.html", context=ctx)

def fd_detail(request, pk):
    me = User.objects.get(pk=pk)
    ctx = {
        'me': me
    }
    return render(request, 'friend/friend_detail.html', context=ctx)

def fd_approve(request):
    return HttpResponse('hello')