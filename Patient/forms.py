from django.forms import fields
from accounts.models import PatientProfile
from django import forms


class PatientProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PatientProfileForm, self).__init__(*args, **kwargs)
        self.fields['Address'].widget.attrs = {'class': 'form-control','placeholder':'Enter your address'}
        self.fields['Mobile'].widget.attrs = {'class': 'form-control','placeholder':'Enter your Mobile number'}
        self.fields['Date_Of_Birth'].widget.attrs = {'class': 'form-control','placeholder':'Enter your Date of birth'}
        self.fields['Blood_Group'].widget.attrs = {'class': 'form-control','placeholder':'Enter your address'}
        self.fields['city'].widget.attrs = {'class': 'form-control','placeholder':'Enter your city'}
        self.fields['District'].widget.attrs = {'class': 'form-control','placeholder':'Enter your district'}
        self.fields['Country'].widget.attrs = {'class': 'form-control','placeholder':'Enter your country'}
        self.fields['profile_image'].widget.attrs = {'class': 'upload'}
        self.fields['Gender'].widget.attrs = {'class': 'form-control select','required':True}

    class Meta:
        model = PatientProfile  
        fields = ['user','Address','Mobile','profile_image','Date_Of_Birth','Blood_Group','city','District','Country','Gender',]
