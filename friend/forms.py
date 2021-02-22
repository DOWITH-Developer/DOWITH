from django.contrib.auth.forms import UserCreationForm
from .models import Friendship
from django import forms


class FriendshipForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = '__all__'
        
class FriendSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')