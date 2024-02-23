from django.contrib import admin
from django.urls import path
from .views import menu_view, home

urlpatterns = [
    path('home/', home, name='home'),
    path('menu/', menu_view, name='menu'),
]