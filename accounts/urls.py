from django.urls import path
from . import views 


app_name = 'accounts'

urlpatterns = [
    path('login/',views.LoginView.as_view(),name="login"),
    path("Patient-signup/", views.Patient_register.as_view(), name="patientsignup"),
    path("Doctor-signup/", views.Doctor_register.as_view(), name="doctorsignup"),
    path("logout/", views.logout_view, name="logout")
]
