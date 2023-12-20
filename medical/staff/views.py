# staffs/views.py

from django.shortcuts import render, redirect, get_object_or_404

from patient.models import Doctor, Nurse, Surgeon
from .models import StaffMember
from .forms import StaffMemberForm

def add_remove_staff_member(request):
    
    if request.method == 'POST':
        form = StaffMemberForm(request.POST)
        if form.is_valid():
            form.save()

            if request.POST['job_type'] == "Doctor":
                b = Doctor(name=request.POST['name'], specialization=request.POST['specialization'] , contact_number=request.POST['phone_number'],email=request.POST['email'])
                b.save()
            elif request.POST['job_type'] == "Nurse":
                b = Nurse(name=request.POST['name'], specialization=request.POST['specialization'] , contact_number=request.POST['phone_number'],email=request.POST['email'],shift_time=request.POST['shift_time'],end_time=request.POST['end_time'])
                b.save()
                
            elif request.POST['job_type'] == "Surgeon":
                b = Surgeon(name=request.POST['name'], specialization=request.POST['specialization'] , contact_number=request.POST['phone_number'],email=request.POST['email'])
                b.save()
                
            return redirect('view_staff_members')
    else:
        form = StaffMemberForm()

    context = {
        'form': form,
    }

    return render(request, 'staffs/add_remove_staff_member.html', context)

def view_staff_members(request, job_type=None):
    try:
        job_type = request.GET['job_type']
    except:
        pass
    if job_type:
        staff_members = StaffMember.objects.filter(job_type=job_type)
    else:
        staff_members = StaffMember.objects.all()
    print(staff_members)
    context = {
        'staff_members': staff_members,
        'selected_job_type': job_type,
    }
    print(context)
    return render(request, 'staffs/view_staff_members.html', context)


