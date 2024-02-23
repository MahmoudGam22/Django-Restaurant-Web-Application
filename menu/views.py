from django.shortcuts import render
from .models import MenuItem
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'menu/home.html')


def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'menu_items': menu_items})
