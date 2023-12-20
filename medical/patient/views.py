# patient_management/views.py

import datetime
from django.shortcuts import render, redirect

from in_patient.forms import loginForm
from .models import Patient, Appointment, PatientHistory
from .forms import PatientForm, AppointmentForm,DoctortForm,PatientHistoryForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout

today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)


 

def register(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        role=request.POST.get("role")
        password=request.POST.get("password")
        
        
        if User.objects.filter(email=email).exists():
          
          return render(request,'Accounts/register.html',{"message":"User Already Exist"})
        else:
            
            created = User.objects.create_user(username=email,email=email,first_name=firstname,last_name=lastname,password=password)
            auth_login(request,created)
            user=request.user
            return redirect('dashboard')
    else:
        print(type(User))
        return render(request,'Accounts/register.html')


def login(request):
        if request.method=="POST":
            
            username = request.POST["username"]
            password = request.POST["password"]
            user= authenticate(username=username,password=password)
            if user is not None:
                print("Login done")
                auth_login(request,user)
                
                
                return redirect('dashboard')
            else:
                return render(request,'Accounts/login.html',{'message':"Username Or Password Is Incorrect"})
        
        else:
            if request.user.is_authenticated:
                user=request.user
                print(user)

                
                return redirect('dashboard')
                
            else:
                return render(request,'Accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')



def dashboard(request):
    context = {"user": request.user.first_name}
    return render(request,'Accounts/dashboard.html',context)


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_patient')
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

def patient_data(request):
    patient = Patient.objects.all()
    return render(request, 'patients/patient_data.html', {'patient': patient})

def patient_history(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        phone = request.POST['phone']
        patient = Patient.objects.filter(name=name,dob=dob)
        if patient is not None:
            id = patient[0].id
            return redirect(f'/view_patient/{id}?history=yes')
        
    return render(request, 'patients/patient_history.html')

def view_patient(request, patient_id):
    if request.method == 'POST':
        form = PatientHistoryForm(request.POST)
        appointment_id=request.POST['appointment']
        if form.is_valid():
            form.save()
            a = Appointment.objects.get(id=appointment_id)
            a.status = "C"
            a.save()
            return redirect('scheuled')
        else:
            print(form.is_valid())
            appointments = Appointment.objects.filter(date__range=(today_min, today_max)).order_by('-id')
            return render(request, 'doctor/scheuled.html', {'appointments':appointments})
    else:
        is_history = "no"
        try:
            is_history = request.GET['history']
        except Exception as e:
            print(e)
        patient = Patient.objects.get(id=patient_id)
        print(patient)
        appointment_data = Appointment.objects.filter(patient=patient).order_by('-id')
        n = appointment_data.count()
        status = "new"
        doctor = None
        appointments = []
        last_appointment = None
        if appointment_data is not None:
            status = "old"
            appointments_info = {}
            for appointment in appointment_data:
                last = "False"
                
                appointments_info['order'] = appointment.id
                appointments_info['date'] = appointment.date
                appointments_info['time'] = appointment.time
                appointments_info['doctor'] = appointment.doctor
                doctor = appointment.doctor
                
                if n-1 == 0 :
                    print("history:::",is_history)
                    if is_history == "yes":
                        appointments_info['last'] = 'None'
                    else:
                        appointments_info['last'] = 'True'
                else:
                    appointments_info['last'] = last
                    
                try :
                    text = "Data"
                    last_appointment = appointment.id
                    history = PatientHistory.objects.get(appointment=appointment.id)
                    appointments_info['diagnosis'] = history.diagnosis
                    appointments_info['illness'] = history.illness
                    appointments_info['treatment'] = history.treatment
                    appointments_info['prescription'] = history.prescription
                    appointments_info['text'] = text
                except Exception as e:
                    text = "No Data"
                    appointments_info['text'] = text
                appointments.append(appointments_info.copy())
                n = n-1
        form = PatientHistoryForm(initial={'patient': patient.id,'appointment':last_appointment,'doctor':doctor})    
        data = {'patient': patient,
                'appointments_info':appointments,
                'status':status,
                'form':form}
        print(data)
        return render(request, 'patients/view_patient.html', data)
       

def add_doctor(request):
    if request.method == 'POST':
        form = DoctortForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_doctor')
    else:
        form = DoctortForm()
    return render(request, 'patients/add_doctor.html', {'form': form})
# Add views for scheduling appointments, checking diagnoses, and viewing appointments per doctor and per day as needed


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment')
    else:
        form = AppointmentForm()
        appointments = Appointment.objects.all().order_by('-id')
        return render(request, 'patients/appointment.html', {'form': form,'appointments':appointments})

   
def scheuled(request):
    appointments = Appointment.objects.filter(date__range=(today_min, today_max),status="Booked").order_by('-id')
    
    return render(request, 'doctor/scheuled.html', {'appointments':appointments})

