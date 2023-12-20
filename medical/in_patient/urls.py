# patient_management/urls.py

from django.urls import path
from .views import (
    check_available_room_bed,
    assign_remove_patient,
    assign_remove_doctor,
    room_management,
    # assign_remove_nurse,
    view_scheduled_surgery_per_room,
    view_scheduled_surgery_per_surgeon,
    book_surgery,
    view_scheduled_surgery_per_patient,
    
)

urlpatterns = [
        path('check_available_room_bed/', check_available_room_bed, name='check_available_room_bed'),
    path('room-management/', room_management, name='room_management'),
    path('assign_remove_patient/', assign_remove_patient, name='assign_remove_patient'),
    path('assign_remove_doctor/', assign_remove_doctor, name='assign_remove_doctor'),
    path('view_scheduled_surgery_per_room/', view_scheduled_surgery_per_room, name='view_scheduled_surgery_per_room'),
    path('view_scheduled_surgery_per_surgeon/', view_scheduled_surgery_per_surgeon, name='view_scheduled_surgery_per_surgeon'),
    path('book_surgery/', book_surgery, name='book_surgery'),
    path('view_scheduled_surgery_per_patient/', view_scheduled_surgery_per_patient, name='view_scheduled_surgery_per_patient'),
]
