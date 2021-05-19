from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

Gender_CHOICES= [
('Male', 'Male'),
('Female', 'Female'),
]


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_Doctor = models.BooleanField(default=False)
    username = models.CharField(
        max_length=30, unique=False, null=True, blank=True)
    email = models.CharField(max_length=30, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta(object):
        unique_together = ('email',)


class PatientProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='client_profile')
    Address = models.CharField(max_length=100, null=True, blank=True)
    Mobile = PhoneNumberField(
        max_length=10, blank=False, unique=True, null=True)
    profile_image = models.ImageField(
        default='default.png', null=True, upload_to='profile_pics')
    Date_Of_Birth = models.DateField(auto_now_add=False, null=True, blank=True)
    Blood_Group = models.CharField(max_length=50,null=True, blank=True)
    city = models.CharField(max_length=50,null=True, blank=True)
    District = models.CharField(max_length=150,null=True, blank=True)
    Country = models.CharField(max_length=150,null=True, blank=True)
    Gender = models.CharField(max_length=150,choices=Gender_CHOICES,default='Male')

    def __str__(self):
        return self.user.email


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='doctor_profile')
    Address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(
        max_length=10, blank=False, unique=True, null=True)
    profile_image = models.ImageField(
        default='default.png', null=True, upload_to='profile_pics')
    city = models.CharField(max_length=50,null=True,blank=True)
    State = models.CharField(max_length=50,null=True,blank=True)
    Country = models.CharField(max_length=50,null=True,blank=True)
    Gender = models.CharField(max_length=50,null=True,blank=True)
    Date_of_Birth = models.DateField(auto_now_add=False,null=True,blank=True)
    biography = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.user.email
