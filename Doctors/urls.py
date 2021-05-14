from django.urls import  path
from . import views 

app_name="doctors"

urlpatterns = [
    path('Doctor-dashboard/',views.Dashboard,name='Doctordashboard'),
    path('Doctor-appointments/',views.Appointments,name='DoctorAppointments'),
    path('Doctor-patients/',views.patients,name='DoctorPatients'),
    path('Doctor-profile/',views.DoctorProfile,name='DoctorProfile'),
    path('Doctor-password/',views.ChangePaword,name="passwordchange"),
]
