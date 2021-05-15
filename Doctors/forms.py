from django import forms
from .models import *



class DoctorprofileForm(forms.ModelForm):
    
    class Meta:
        model = Doctorprofile
        fields = ("Doctor","Clinic_name","Clinic_Address","Services","Degree","college","yearDonne","Hospital_name","from_year","to_year","Designation","Award_got","year",)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['Clinic_name'].widget.attrs.update(
                {'placeholder': 'Enter clinic Name', 'class': 'form-control'})