# patient_management/forms.py

from django import forms
from .models import StaffMember

class TimeInput(forms.DateInput):
    input_type = 'time'
    
class DateInput(forms.DateInput):
    input_type = 'date'

class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = '__all__' 
        widgets = {
            'shift_time':TimeInput(),
            'end_time':TimeInput(),
            'date_of_birth':DateInput(),
            'joining_date':DateInput(),
            'termination_date':DateInput(),
        }
