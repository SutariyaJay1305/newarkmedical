# patient_management/models.py

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    SSN = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    gender = models.BooleanField() #Male for 1 and Female for 0
    # Add other patient-related fields as needed

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    # Add other doctor-related fields as needed

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    # Add other appointment-related fields as needed
