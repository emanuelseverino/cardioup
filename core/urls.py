from django.contrib import admin
from django.urls import path

from core.views import IndexView, logout_user

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('logout/', logout_user, name='sair'),
]
