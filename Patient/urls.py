from django.urls import path,include
from . import views

app_name="patient"

urlpatterns = [
    path("Patient/", views.PatientDashboard, name="PatientDashboard"),
    path("Profile/", views.Profile, name="profile"),
    path("favourites/", views.Favourites, name="favourites"),
    path("search-doctor/", views.SearchDoctor, name="search"),
    path("book-doctor/", views.Booking, name="booking"),
    path("book-sucess/", views.BookingSuccess, name="bookingsucess"),
    path("book-payments/", views.Payments, name="Payments"),
    path("enter-info/", views.EnterUserinfo, name="enterinfo"),
]
