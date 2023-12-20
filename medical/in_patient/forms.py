# patient_management/forms.py

from django import forms
from .models import InPatientManagement, SurgerySchedule


class DateInput(forms.DateInput):
    input_type = 'date'
    
class TextInput(forms.TextInput):
    input_type = 'text'

class loginForm(forms.Form):
    username=forms.CharField(help_text="Enter UserName",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),label="Enetr User Name",error_messages={'error':"Username Can not be empty"},max_length=50)
    password=forms.CharField(help_text="Enter Password",required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),label="Password",error_messages={'error':"Password Can not be empty"},max_length=12)


class BookRoomForm(forms.ModelForm):
    class Meta:
        model = InPatientManagement
        fields = ['patient','room_number','bed_number','assigned_doctor','assigned_nurse','bed_booked_date']
        widgets = {
            'bed_booked_date': DateInput(),
        }
class RemoveRoomForm(forms.ModelForm):
    class Meta:
        model = InPatientManagement
        fields = '__all__'
        widgets = {
            'bed_booked_date': DateInput(),
            'bed_remove_date': DateInput(),
        }

class AssignPatientForm(forms.ModelForm):
    class Meta:
        model = InPatientManagement
        fields = '__all__'

class AssignDoctorForm(forms.ModelForm):
    class Meta:
        model = InPatientManagement
        fields = '__all__'

# class AssignNurseForm(forms.ModelForm):
#     class Meta:
#         model = InPatientManagement
#         fields = ['assigned_nurse']

class SurgeryBookingForm(forms.ModelForm):
    class Meta:
        model = SurgerySchedule
        fields = '__all__'
        widgets = {
            'scheduled_date': DateInput(),
            'scheduled_surgery_date': DateInput(),
        }
