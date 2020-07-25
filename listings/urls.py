from django.contrib import admin
from django.urls import path
from . import views

"""The `urlpatterns` list routes URLs to views. """

urlpatterns = [
    #name is name of the view i.e the template
    #empty string meaning home page i.e landing url
    path('', views.index, name="listings"),
    #dyanmic urls example: /listing/1
    path('<int:listing_id>', views.listing, name="listing"),
    path('search', views.search, name="search"),
]