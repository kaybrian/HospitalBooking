from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View


def PatientDashboard(request):
    context = { }
    return render (request, 'Patient/dashboard.html',context)



class Profile(View):
    template_name = "Patient/profile.html"
    # form_class = LoginForm

    def get(self, request, *args, **kwargs):
        # form = self.form_class()
        context = {}
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     email = request.POST.get('email_address')
    #     password = request.POST.get('password')

    #     user = authenticate(request, email=email, password=password)

    #     if user is not None and user.is_patient:
    #         login(request, user)
    #         return redirect('patient:PatientDashboard')
    #     elif user is not None and user.is_Doctor:
    #         return HttpResponse("Logined in the Doctor")
    #     else:
    #         return HttpResponse("Sorry No such user")



def Favourites(request):
    context = {}
    return render(request,'Patient/favourites.html',context)