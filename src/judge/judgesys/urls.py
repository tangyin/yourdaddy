#coding=utf8

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^index/$', views.index, name="index"),
]