from django.urls import path,include
from . import views

app_name="patient"

urlpatterns = [
    path("Patient/", views.PatientDashboard, name="PatientDashboard"),
    path("Profile/", views.Profile, name="profile"),
    path("favourites/", views.Favourites, name="favourites"),
]
