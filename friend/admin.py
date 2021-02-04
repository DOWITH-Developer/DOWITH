from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ['creator', 'follower']
    list_display_links = ['creator', 'follower']