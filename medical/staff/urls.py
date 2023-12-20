# patient_management/urls.py

from django.urls import path
from .views import add_remove_staff_member, view_staff_members

urlpatterns = [
    path('add_remove_staff_member/', add_remove_staff_member, name='add_remove_staff_member'),
    path('view_staff_members/', view_staff_members, name='view_staff_members'),
    path('view_staff_members/<str:job_type>/', view_staff_members, name='view_staff_members_by_type'),
]
