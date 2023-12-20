# patient_management/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('add-patient/', views.add_patient, name='add_patient'),
    path('patient-data/', views.patient_data, name='patient_data'),
    path('patient-history/', views.patient_history, name='patient_history'),
    path('view_patient/<int:patient_id>/', views.view_patient, name='view_patient'),
    
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('appointment/', views.appointment, name='appointment'),
    path('scheuled/', views.scheuled, name='scheuled'),
    # Add additional paths for scheduling appointments, checking diagnoses, and viewing appointments per doctor and per day
]
