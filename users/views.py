from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form. 
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
    
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

