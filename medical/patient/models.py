# patient_management/models.py

from django.db import models
from django import forms 
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )




class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    dob = models.DateField()
    SSN = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
    # Add other patient-related fields as needed


class Nurse(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    shift_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    # Add other relevant fields for the Doctor model

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    # Add other relevant fields for the Doctor model

    def __str__(self):
        return self.name
    

class Surgeon(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    # Add other relevant fields for the Doctor model

    def __str__(self):
        return self.name

STATUS_CHOICES = (
        ('Booked', 'Booked'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default=STATUS_CHOICES[0][1])
    # Add other appointment-related fields as needed

class PatientHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    illness = models.CharField(max_length=100)
    treatment = models.TextField()
    prescription = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    date_recorded = models.DateField(auto_now_add=True)
    # Add other relevant fields for the PatientHistory model

    def __str__(self):
        return f"{self.patient.name} - {self.illness} - {self.date_recorded}"
    

