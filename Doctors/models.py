from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings


class Doctorprofile(models.Model):
    Doctor =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clinic')
    Clinic_name = models.CharField(max_length=150,null=True,blank=True)
    Clinic_Address =models.CharField(max_length=150,null=True,blank=True)
    Services = TaggableManager()
    Degree = models.CharField(max_length=450,null=True,blank=True)
    college = models.CharField(max_length=350, null=True,blank=True)
    yearDonne = models.DateField(auto_now_add=False,null=True,blank=True)
    Hospital_name = models.CharField(max_length=450,null=True,blank=True)
    from_year = models.DateField(auto_now_add=False,null=True,blank=True)
    to_year = models.DateField(auto_now_add=False,null=True,blank=True)
    Designation = models.CharField(max_length=450,null=True,blank=True)
    Award_got = models.CharField(max_length=450,null=True,blank=True)
    year = models.DateField(auto_now_add=False,null=True,blank=True)

    def __str__(self):
        return self.Doctor
    


class Prescriptions(models.Model):
    Doctor =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='prescriptions')
    patient = models.ManyToManyField('Patient.Patientsprofile', related_name='prescrip')
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=450, null=True,blank=True)
    Diagonis = models.CharField(max_length=50)
    billing = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return self.Name 
    

class MedicialRecords(models.Model):
    Doctor =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='records')
    patient = models.ManyToManyField('Patient.Patientsprofile', related_name='records')
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=450, null=True,blank=True)
    Description = models.CharField(max_length=50)
    Attachment = models.FileField(upload_to='files', max_length=100,null=True,blank=True)

    def __str__(self):
        return self.Name
    




