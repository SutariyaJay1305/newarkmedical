# patient_management/models.py

from django.db import models
from patient.models import Nurse, Patient, Doctor, Surgeon#, Nurse

ROOM_TYPE = (
        ('Shared', 'Shared'),
        ('Private', 'Private'),
        ('Surgery', 'Surgery'),
    )

    

class Rooms(models.Model):
    room_number  = models.IntegerField(unique=True)
    bed_number_1 = models.BooleanField(default=False)
    bed_number_2 = models.BooleanField(default=False)
    room_type =  models.CharField(max_length=10, choices=ROOM_TYPE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room- {self.id} -{self.room_type} "

class InPatientManagement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room_number = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, blank=True)
    bed_number = models.IntegerField()
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    assigned_nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, null=True, blank=True)
    bed_booked_date = models.DateField(null=True, blank=True)
    bed_remove_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"InPatientManagement - {self.patient.name}"

class SurgerySchedule(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scheduled_surgery_room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    surgeon = models.ForeignKey(Surgeon, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    scheduled_surgery_date = models.DateField(null=True, blank=True)
    surgery_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"  {self.scheduled_surgery_room}, Surgeon {self.surgeon.name}, Date {self.scheduled_date}"
