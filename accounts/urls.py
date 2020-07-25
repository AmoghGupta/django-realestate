from django.contrib import admin
from django.urls import path
from . import views

# After adding a url path in the urls file, and defining 
# corresponding view function to deal with it, If we want to access this 
# same url through views in some place else, or maybe in the template file of your 
# html pages, you do that using name and namespace in your code to access it, just 
# like variable names. This helps because defining another url path and/or using direct 
# links, makes the code more difficult to main


urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),

]