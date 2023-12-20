from django.contrib import admin
from .models import Rooms,InPatientManagement,SurgerySchedule

# Register your models here.

class RoomsAdmin(admin.ModelAdmin):
    pass
class InPatientManagementAdmin(admin.ModelAdmin):
    pass
class SurgeryScheduleAdmin(admin.ModelAdmin):
    pass




admin.site.register(Rooms, RoomsAdmin)
admin.site.register(InPatientManagement, InPatientManagementAdmin)
admin.site.register(SurgerySchedule, SurgeryScheduleAdmin)

