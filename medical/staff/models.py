# patient_management/models.py

from django.db import models

class StaffMember(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    STATUS = [
        ('Active', 'Active'),
        ('Non_Acive', 'Non_Acive'),
        ('Holiday', 'Holiday'),
    ]

    JOB_TYPES = [
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Surgeon', 'Surgeon'),
        ('Physician Assistant', 'Physician Assistant'),
        ('Pharmacist', 'Pharmacist'),
        ('Medical Technologist', 'Medical Technologist'),
        ('Radiologist', 'Radiologist'),
        ('Physical Therapist', 'Physical Therapist'),
        ('Occupational Therapist', 'Occupational Therapist'),
        ('Speech-Language Pathologist', 'Speech-Language Pathologist'),
        ('Administrative Staff', 'Administrative Staff'),
        ('Maintenance and Support Staff', 'Maintenance and Support Staff'),
        # Add more job types as needed
    ]

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    specialization = models.CharField(max_length=100)


    job_type = models.CharField(max_length=100, choices=JOB_TYPES)
    # department = models.CharField(max_length=255)
    # employee_id = models.CharField(max_length=10, unique=True)

    shift_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    # schedule_job_shift = models.BooleanField(default=False)

    ssn = models.CharField(max_length=11, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)

    qualifications = models.TextField(blank=True, null=True)
    license_certification = models.CharField(max_length=255, blank=True, null=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)

    blood_type = models.CharField(max_length=5, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)

    joining_date = models.DateField()
    status  = models.CharField(max_length=10, choices=STATUS)
    termination_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.job_type}"
