from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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