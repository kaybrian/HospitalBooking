from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url='/accounts/login/')
def Dashboard(request):
    context = {}
    return render(request,'Doctors/dashboard.html',context)

@login_required(login_url='/accounts/login/')
def Appointments(request):
    context = {}
    return render(request,'Doctors/appointments.html',context)

@login_required(login_url='/accounts/login/')
def patients(request):
    context = {}
    return render(request,'Doctors/my-patients.html',context)


@login_required(login_url='/accounts/login/')
def DoctorProfile(request):
    context = {}
    return render(request,'Doctors/profile.html',context)


@login_required(login_url='/accounts/login/')
def ChangePaword(request):
    context = {}
    return render(request,'Doctors/passwordchange.html',context)

