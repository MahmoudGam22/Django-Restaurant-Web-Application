from django.contrib import admin
from django.urls import path
from .views import reserve_table, reservation_success

urlpatterns = [
    path('reserve/', reserve_table, name='reserve_table'),
    path('reservation_success/', reservation_success, name='reservation_success'),
]