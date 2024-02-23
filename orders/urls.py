from django.contrib import admin
from django.urls import path
from .views import menu_view, order_view

urlpatterns = [
    path('menu_view/', menu_view, name='menu_view'),
    path('order/', order_view, name='order_view'),
]