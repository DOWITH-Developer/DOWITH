from django.urls import path, include
from .views import *

app_name='friend'

urlpatterns = [
    path('list/', fd_list, name="fd_list"),
    path('create/', fd_create, name="fd_create"),
    path('detail/<int:pk>', fd_detail, name="fd_detail"),
    path('approve/<int:pk>', fd_approve, name="fd_approve"),
    path('delete/<int:pk>', fd_delete, name="fd_delete"),
]
