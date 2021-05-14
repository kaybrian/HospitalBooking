from django.views import View
from .forms import *
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from.models import *




class Patient_register(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'accounts/patientsignup.html'

    def validate(self, form):
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        

        if form.is_valid():
            if password1 == password2:
                user = User.objects.create(
                    username=username, email=email, password=password1)
                user.save()
                user = authenticate(email=email, password=password1)

    # def get_success_url(self):
    #     return reverse('cilenthome')



class Doctor_register(CreateView):
    model = User
    form_class = MechanicSignUpForm
    template_name = 'accounts/doctor.html'

    def validate(self, form):
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        
        print(password2)
        print(password1)
        print(email)
        print(username)

        if form.is_valid():
            if password1 == password2:
                user = User.objects.create(
                    username=username, email=email, password=password1)
                user.save()


class LoginView(View):
    template_name = "accounts/login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        email = request.POST.get('email_address')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_patient:
            login(request, user)
            return redirect('patient:PatientDashboard')

        elif user is not None and user.is_Doctor:
            login(request, user)
            return redirect('doctors:Doctordashboard')
        else:
            return redirect('accounts:login')


def logout_view(request):
    logout(request)
    return redirect('landing:index')
