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
        return self.Clinic_name
    


# class Works(models.Model):
#     Doctor =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='works')
   


# class Education(models.Model):
#     Doctor =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='education')
   

#     def __str__(self):
#         return self.Degree
    

# class Experience(models.Model):
#     Doctor =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='experience')
    

#     def __str__(self):
#         return self.Hospital_name
    

# class Awards(models.Model):
#     Doctor =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='awards')
    

#     def __str__(self):
#         return self.Award_got
    




