from django.contrib import admin
from django.urls import path, include
from twitterApp import views

urlpatterns = [
    path('', views.base , name = "base"), 
    path('home', views.home , name = "home1"), 

]
