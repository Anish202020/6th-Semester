from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.shortcuts import HttpResponse
from . import views
urlpatterns = [
path('', views.home, name ='index'),
]