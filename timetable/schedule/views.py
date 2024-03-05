from django.shortcuts import render, get_object_or_404,redirect
import pandas as pd
from .models import *
from .forms import StudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def new(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = StudentForm()
    return render(request, 'schedule/new.html', {'form': form})

def edit(request, student_id):
    # Retrieve the existing data
    existing_data = Student.objects.get(pk=student_id)

    if request.method == 'POST':
        # If the form is submitted, process the form data
        form = StudentForm(request.POST, instance=existing_data)
        if form.is_valid():
            form.save()
            # Redirect back to the index page after successful form submission
            return HttpResponseRedirect(reverse("index"))  # Replace 'index' with the actual URL name of your index view
    else:
        # If it's a GET request, display the form with existing data
        form = StudentForm(instance=existing_data)

    return render(request, 'schedule/edit.html', {'form': form})

def delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return HttpResponseRedirect(reverse("index"),)

#import timetable from schedule.models
def get_student_timetable(student_id):
    # Get the student
    student = Student.objects.get(pk=student_id)

    # Get the timetable for the student and sort by day
    student_timetable = timetable.objects.filter(student=student).order_by('day')

    # Create a dictionary to store the timetable
    timetable_dict = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    # Add the timetable to the dictionary
    for entry in student_timetable:
        timetable_dict[entry.day].append({
            'unit_name': entry.unit.unit_name,
            'time': entry.time,
            'venue': entry.venue,
        })
    
    # Convert the dictionary to a pandas DataFrame
    timetable_df = pd.DataFrame(timetable_dict)

    return timetable_df



def index(request):
    # show student on index page
    students = Student.objects.all()
    return render(request, 'schedule/index.html', {'students': students})

