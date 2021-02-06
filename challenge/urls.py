from django.urls import path, include
from .views import *

app_name = 'challenge'

urlpatterns = [
    path('<int:pk>/', challenge_detail, name='challenge_detail'),
    path('create/', challenge_create, name='challenge_create'),
    path('<int:pk>/delete/', challenge_delete, name='challenge_delete'),
    path('success/', success, name='success'),
    path('list/', view=ch_list, name='ch_list'),
]
