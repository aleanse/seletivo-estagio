from django.urls import path
from django.contrib import admin

from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
]
