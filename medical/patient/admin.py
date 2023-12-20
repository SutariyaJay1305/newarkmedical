from django.contrib import admin
from .models import Nurse, Patient,Doctor,Appointment,PatientHistory,Surgeon

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    pass

class PatientHistoryAdmin(admin.ModelAdmin):
    pass

class DoctorAdmin(admin.ModelAdmin):
    pass
class NurseAdmin(admin.ModelAdmin):
    pass

class AppointmentAdmin(admin.ModelAdmin):
    pass

class SurgeonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Nurse, NurseAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientHistory, PatientHistoryAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Surgeon, SurgeonAdmin)
