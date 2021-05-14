
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('landingpage.urls')),
    path("patients/",include('Patient.urls')),
    path('accounts/',include('accounts.urls')),
    path('Doctors/',include('Doctors.urls')),
]
