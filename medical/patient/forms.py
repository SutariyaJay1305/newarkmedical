# patient_management/forms.py

from django import forms
from .models import Patient, Appointment,Doctor,PatientHistory
from patient import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HiddenInput(forms.DateInput):
    input_type = 'hidden'

class DateInput(forms.DateInput):
    input_type = 'date'
    
class TimeInput(forms.DateInput):
    input_type = 'time'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'dob','SSN','blood_type','address','gender']  # Add other fields as needed

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date','time','reason']  # Add other fields as needed
        widgets = {
            'date': DateInput(),
            'time':TimeInput()
        }

class PatientHistoryForm(forms.ModelForm):
    class Meta:
        model = PatientHistory
        fields = ['patient','appointment','doctor','diagnosis', 'illness', 'treatment','prescription']  # Add other fields as needed
        widgets = {
            'patient': HiddenInput(),
            'appointment':HiddenInput(),
            'doctor':HiddenInput()
        }

# class PatientAppointmentForm(forms.ModelForm):
#     doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
#     class Meta:
#         model=models.Appointment
#         fields=['description','status']


class DoctortForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'contact_number','email']  # Add other fields as needed
        