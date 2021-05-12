from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
    location = models.CharField(max_length=100, null=True, blank=True)
    phone = PhoneNumberField(
        max_length=10, blank=False, unique=True, null=True)
    profile_image = models.ImageField(
        default='default.png', null=True, upload_to='profile_pics')

    def __str__(self):
        return self.user.email


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='doctor_profile')
    location = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(
        max_length=10, blank=False, unique=True, null=True)
    profile_image = models.ImageField(
        default='default.png', null=True, upload_to='profile_pics')

    def __str__(self):
        return self.user.email
