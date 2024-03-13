from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def sign_in(request):
  # Process sign-in logic here (optional)
  # Potentially handle form submission for email/password login (if applicable)
  
  # Redirect to Django-Allauth's login view for Google Sign-In
  return redirect('login')

def index(request):
  if request.user.is_superuser:
    students_list = Students.objects.all()  
    return render(request, 'schedule/index.html', {'students': students_list})
  else:
    return redirect('timetable')

    
def timetable(request):
  # Handle student view logic here
  return render(request, 'timetable.html')
#Show all units
def units(request):
    units_list = Units.objects.all()
    return render(request, 'schedule/units.html', {'units': units_list})

def newstudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            #redirect to index page
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    return render(request, 'schedule/newstudent.html', {'form': form})

def editstudent(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm(instance=student)
    return render(request, 'schedule/editstudent.html', {'form': form})

def deletestudent(request, pk):
    student = get_object_or_404(Students, pk=pk)
    student.delete()
    return HttpResponseRedirect(reverse('index'))

#register new units
def newunit(request):
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.save()
            return HttpResponseRedirect(reverse('units'))
    else:
        form = UnitForm()
    return render(request, 'schedule/newunit.html', {'form': form})

#edit units
def editunit(request, pk):
    unit = get_object_or_404(Units, pk=pk)
    if request.method == "POST":
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.save()
            return HttpResponseRedirect(reverse('units'))
    else:
        form = UnitForm(instance=unit)
    return render(request, 'schedule/editunit.html', {'form': form})

def deleteunit(request, pk):
    unit = get_object_or_404(Units, pk=pk)
    unit.delete()
    return HttpResponseRedirect(reverse('index'))

def courses(request):
    courses_list = Courses.objects.all()
    return render(request, 'schedule/courses.html', {'courses': courses_list})

def editcourse(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return HttpResponseRedirect(reverse('courses'))
    else:
        form = CourseForm(instance=course)