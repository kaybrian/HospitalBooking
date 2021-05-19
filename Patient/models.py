from django.db import models
from django.conf import settings
from Doctors.models import Doctorprofile
from django.template.defaultfilters import slugify



class Patientsprofile(models.Model):
    patientname =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pateintprofile')
    age = models.PositiveSmallIntegerField(null=True,blank=True)

    def __str__(self):
        return self.patientname
    


class Appointments(models.Model):
    patient =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Appoitments')
    Doctor = models.ForeignKey(Doctorprofile, on_delete=models.CASCADE, related_name='doctor')
    appointment_date = models.DateField(auto_now_add=False)
    booking = models.DateField(auto_now_add=True)
    price = models.CharField(max_length=50)
    flowup = models.DateField(auto_now_add=False,null=True,blank=True)
    status = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, unique_for_date="appointment_date")
    accepted = models.BooleanField(default=False)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Appointment of {self.patient}'

    class Meta:
        ordering = ['-appointment_date']

    


