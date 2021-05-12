from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, PatientProfile, DoctorProfile
from django.db import transaction
from django import forms


class ClientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email Address', 'class': 'form-control floating'})
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username', 'class': 'form-control floating'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password', 'class': 'form-control floating'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm Password', 'class': 'form-control floating'})

        def clean_email(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            if email and User.objects.filter(email=email).exclude(username=username).exists():
                raise forms.ValidationError(u'Email addresses must be unique.')
            return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        client = PatientProfile.objects.create(user=user)
        client.save()
        return client


class MechanicSignUpForm(UserCreationForm):
    password = forms.CharField(max_length=80, widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email Address', 'class': 'form-control'})
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm Password', 'class': 'form-control'})

        def clean_email(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            if email and User.objects.filter(email=email).exclude(username=username).exists():
                raise forms.ValidationError(
                    u'Email ad dresses must be unique.')
            return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_Doctor = True
        user.save()
        Doctor = DoctorProfile.objects.create(user=user)
        Doctor.save()
        return Doctor


class LoginForm(forms.Form):
    email_address = forms.EmailField(label="Email Address", max_length=255,)
    email_address.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Email Address'})
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)
    password.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Password'})
