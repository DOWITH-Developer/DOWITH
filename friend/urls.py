from django.urls import path, include
from .views import *

app_name='friend'

urlpatterns = [
    path('list/<int:pk>', fd_list, name="fd_list"),
    path('create/<int:pk>', fd_create, name="fd_create"),
    path('detail/<int:pk>', fd_detail, name="fd_detail"),
    path('approve/', fd_approve, name="fd_approve"),
    path('more/<int:pk>/',fd_more, name="fd_more"),
]
