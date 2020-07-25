from django.contrib import admin
from django.urls import path
from . import views

"""The `urlpatterns` list routes URLs to views. """

urlpatterns = [
    #empty string meaning home page i.e landing url
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
]