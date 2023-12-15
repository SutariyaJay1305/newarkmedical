# patient_management/views.py

from django.shortcuts import render, redirect
from .models import Patient, Appointment
from .forms import PatientForm, AppointmentForm

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

def view_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'patients/view_patient.html', {'patient': patient, 'appointments': appointments})

# Add views for scheduling appointments, checking diagnoses, and viewing appointments per doctor and per day as needed
