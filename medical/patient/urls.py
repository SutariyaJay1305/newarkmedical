# patient_management/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add_patient/', views.add_patient, name='add_patient'),
    path('view_patient/<int:patient_id>/', views.view_patient, name='view_patient'),
    # Add additional paths for scheduling appointments, checking diagnoses, and viewing appointments per doctor and per day
]
