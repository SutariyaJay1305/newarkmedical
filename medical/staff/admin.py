from django.contrib import admin
from .models import StaffMember

# Register your models here.

class StaffMemberAdmin(admin.ModelAdmin):
    pass




admin.site.register(StaffMember, StaffMemberAdmin)

