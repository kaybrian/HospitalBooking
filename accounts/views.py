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
        print(password2)
        print(password1)
        print(email)
        print(username)

        if form.is_valid():
            if password1 == password2:
                user = User.objects.create(
                    username=username, email=email, password=password1)
                user.save()
                user = authenticate(email=email, password=password1)

    # def get_success_url(self):
    #     return reverse('cilenthome')



# class Mechanic_register(CreateView):
#     model = User
#     form_class = MechanicSignUpForm
#     template_name = 'accounts/signup2.html'

#     def validate(self, form):
#         password1 = form.cleaned_data.get('password1')
#         password2 = form.cleaned_data.get('password2')
#         username = form.cleaned_data.get('username')
#         email = form.cleaned_data.get('email')

#         if form.is_valid():
#             if password1 == password2:
#                 user = User.objects.create(
#                     username=username, email=email, password=password1)
#                 user.save()

    # we are left to login in the users and redirecting them to thier respect page views
    # a function to validate the form sent in form the user and alsowe nee to find the differnt pages


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

        # if user is not None and user.is_client:
        #     login(request, user)
        #     return HttpResponseRedirect(reverse('cilenthome'))
        # elif user is not None and user.is_mechanic:
        #     return HttpResponse("Logined in the mechanic user")
        # else:
        #     return HttpResponse("Sorry No such user")


def logout_view(request):
    logout(request)
    return render(request, '/')
