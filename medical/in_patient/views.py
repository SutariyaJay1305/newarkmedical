# views.py

import datetime
from django.shortcuts import render,redirect
from django.db.models import Count
from in_patient.forms import AssignDoctorForm, AssignPatientForm, BookRoomForm, RemoveRoomForm, SurgeryBookingForm, loginForm
from patient.models import Patient #,AssignNurseForm
from .models import InPatientManagement, SurgerySchedule, Rooms
from django.contrib.auth import authenticate,login as auth_login,logout






def check_available_room_bed(request):
    # Assuming you have a total number of rooms and beds
    available_shared_rooms = Rooms.objects.filter(room_type='Shared')
    available_private_rooms = Rooms.objects.filter(room_type='Private')
    available_surgery_rooms = Rooms.objects.filter(room_type='Surgery')


    context = {
        'available_shared_rooms': available_shared_rooms,
        'available_private_rooms': available_private_rooms,
        'available_surgery_rooms': available_surgery_rooms, 
        # 'available_beds': available_beds,
    }

    return render(request, 'patient_management/check_available_room_bed.html', context)

def room_management(request):
    room =None
    bed =None
    
    if request.method == 'POST':
        try:
            is_booked = request.GET['is_booked']
            room = request.GET['room']
            room = Rooms.objects.get(room_number=room)
            bed = request.GET['bed']
        except Exception as e:
            print(e)
            pass

        if is_booked == "false":
            form = BookRoomForm(request.POST)
        else:
            form = RemoveRoomForm(request.POST)
        if form.is_valid():
            form.save()
            if room.room_type != "Shared":
                room.is_available =False
            else:
                if bed == "1":
                    room.bed_number_1 = True
                    if room.bed_number_2 == True:
                        room.is_available =False
                else:
                    room.bed_number_2 = True
                    if room.bed_number_1 == True:
                        room.is_available =False
            

            room.save()
                
            

  
        return redirect('check_available_room_bed')

    else:
        try:
            room = request.GET['room']
            room = Rooms.objects.get(room_number=room)
            room_id = (room.id)
            bed = request.GET['bed']
            is_booked = request.GET['is_booked']
            if bed == 1:
                inital = {'room_number': room,'bed_number':bed}
            else :
                inital = {'room_number': room,'bed_number':bed}
        except Exception as e:
            pass

        if is_booked == "false":
            form = BookRoomForm(initial=inital)
        else:
        
            patient = InPatientManagement.objects.get(room_number=room_id)
            
            inital = {'room_number': room,'bed_number':bed,'patient':patient.patient,'assigned_doctor':patient.assigned_doctor,'assigned_nurse':patient.assigned_nurse,
                    'bed_booked_date':patient.bed_booked_date }
            form = RemoveRoomForm(initial=inital)

        context = {
            'form': form,
            'is_booked': is_booked,
            
        }

        return render(request, 'patient_management/booked_room.html', context)


def assign_remove_patient(request, patient_id=1):
    patient = get_object_or_404(InPatientManagement, patient_id=patient_id)

    if request.method == 'POST':
        form = AssignPatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            # Additional logic if needed
    else:
        form = AssignPatientForm(instance=patient)

    context = {
        'patient': patient,
        'form': form,
    }

    return render(request, 'patient_management/assign_remove_patient.html', context)

def assign_remove_doctor(request, patient_id):
    patient = get_object_or_404(InPatientManagement, patient_id=patient_id)

    if request.method == 'POST':
        form = AssignDoctorForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            # Additional logic if needed
    else:
        form = AssignDoctorForm(instance=patient)

    context = {
        'patient': patient,
        'form': form,
    }

    return render(request, 'patient_management/assign_remove_doctor.html', context)



def view_scheduled_surgery_per_room(request, room_number):
    scheduled_surgeries = SurgerySchedule.objects.filter(room_number=room_number)
    
    context = {
        'room_number': room_number,
        'scheduled_surgeries': scheduled_surgeries,
    }

    return render(request, 'patient_management/view_scheduled_surgery_per_room.html', context)





def view_scheduled_surgery_per_surgeon(request):

    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    try:
        q = request.GET['q']
        scheduled_surgeries_details = SurgerySchedule.objects.filter(surgery_booked=True,scheduled_surgery_date__range=(today_min, today_max),surgeon=q)
        
        date = (datetime.date.today())
        
        context = {
            'scheduled_surgeries': scheduled_surgeries_details,
            'date':date
        }
        print(context)
        return render(request, 'patient_management/view_scheduled_surgery_per_surgon_details.html', context)

    except Exception as e:
        print(e)
        
        scheduled_surgeries = SurgerySchedule.objects.filter(surgery_booked=True,scheduled_surgery_date__range=(today_min, today_max)).values('surgeon__name','surgeon').annotate(count=Count('surgeon'))
                    
        
        date = (datetime.date.today())
        print(scheduled_surgeries)
        
        context = {
            'scheduled_surgeries': scheduled_surgeries,
            'date':date
        }

        return render(request, 'patient_management/view_scheduled_surgery_per_surgon.html', context)

def book_surgery(request):

    if request.method == 'POST':
        form = SurgeryBookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Additional logic if needed
            # return redirect('view_scheduled_surgery_per_patient')
    
    form = SurgeryBookingForm()

    context = {
        'form': form,
    }

    return render(request, 'patient_management/book_surgery.html', context)

def view_scheduled_surgery_per_patient(request, patient_id=None):
    scheduled_surgeries = SurgerySchedule.objects.filter(surgery_booked=True)
    # patient = Patient.objects.filter(id__in=scheduled_surgeries)
    print(scheduled_surgeries)
    
    context = {
        'scheduled_surgeries': scheduled_surgeries,
    }

    return render(request, 'patient_management/view_scheduled_surgery_per_patient.html', context)