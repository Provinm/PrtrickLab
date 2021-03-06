#coding=utf-8

from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'poetry', views.PoetryView.as_view())

# print(router.urls)

urlpatterns = [
    # path(r'upload', views.index),
    path(r'api/', views.PoetryView.as_view()),
    path(r"asr/", views.AsrView.as_view()),
    path(r"tts/", views.TTSView.as_view()),
    path(r"pivot/", views.PivotView.as_view())
]