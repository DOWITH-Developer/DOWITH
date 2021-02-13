from django.urls import path, include
from .views import *

app_name = 'challenge'

urlpatterns = [
    path('<int:pk>/', challenge_detail, name='challenge_detail'),
    path('create/', challenge_create, name='challenge_create'),
    path('delete/<int:pk>/', challenge_delete, name='challenge_delete'),
    path('list/', view=ch_list, name='ch_list'),
    path('calendar/', view=challenge_calendar, name='challenge_calendar'),
    path('enrollment/<int:pk>', challenge_enrollment, name="challenge_enrollment"),
    path('result_ajax/', ResultAjax.as_view(), name="result_ajax"),
]
