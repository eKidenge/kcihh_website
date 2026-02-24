from django.shortcuts import render, redirect
from .models import InvolvementOption
from .forms import VolunteerApplicationForm, DonationForm

def get_involved(request):
    options = InvolvementOption.objects.all().order_by('order')
    return render(request, 'get_involved/index.html', {'options': options})

def volunteer_application(request):
    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_involved')
    else:
        form = VolunteerApplicationForm()
    return render(request, 'get_involved/volunteer.html', {'form': form})

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_involved')
    else:
        form = DonationForm()
    return render(request, 'get_involved/donate.html', {'form': form})