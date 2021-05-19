from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import * 


@login_required(login_url='/accounts/login/')
def PatientDashboard(request):
    context = { }
    return render (request, 'Patient/dashboard.html',context)

@login_required(login_url='/accounts/login/')
def Profile(request):
    context = { }
    return render (request, 'Patient/profile.html',context)


@login_required(login_url='/accounts/login/')
def Favourites(request):
    context = {}
    return render(request,'Patient/favourites.html',context)


@login_required(login_url='/accounts/login/')
def SearchDoctor(request):
    context = {}
    return render(request,'Patient/search.html',context)



@login_required(login_url='/accounts/login/')
def Booking(request):
    context = {}
    return render(request,'Patient/booking.html',context)


@login_required(login_url='/accounts/login/')
def BookingSuccess(request):
    context = {}
    return render(request,'Patient/success.html',context)



@login_required(login_url='/accounts/login/')
def Payments(request):
    context = {}
    return render(request,'Patient/payments.html',context)

@login_required(login_url='/accounts/login/')
def EnterUserinfo(request):
    if request.method == 'POST':
        form = PatientProfileForm(request.POST or None)
    else:
        form = PatientProfileForm()

        
    context = {'form':form,}
    return render(request,'Patient/info.html',context)