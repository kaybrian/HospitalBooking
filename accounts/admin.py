from django.contrib import admin
from .models import DoctorProfile, PatientProfile, User
from django.contrib.auth.admin import UserAdmin
from .forms import *


admin.site.register(User)


admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
