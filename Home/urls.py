from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
   path('', views.index, name="index"),
   path('service', views.service, name="service"),
   path('about', views.about, name="about"),
]