from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

@login_required
def reservation_success(request):
    return render(request, 'reservation/reservation_success.html')

@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
        else:
            print(form.errors)
    else:
        form = ReservationForm()
    context = {'form': form}
    return render(request, 'reservation/reserve_table.html',context)





