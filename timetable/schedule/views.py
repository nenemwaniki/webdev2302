from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

# Sign-in view (redirects to Django-Allauth's login view)
def login(request):
    return render(request, 'schedule/sign_in.html')
# Admin-only view for student list
@login_required
def index(request):
    if request.user.is_superuser:
        students_list = Students.objects.all()
        return render(request, 'schedule/index.html', {'students': students_list})
    else:
        return redirect('home')  # Redirect non-admins to student homepage

# Student-specific homepage
@login_required
def home(request):
    return render(request, 'schedule/home.html')
    
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

@login_required
def editstudent(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.user == student:  # Ensure student is editing their own profile
        if request.method == "POST":
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('home')  # Redirect to student homepage after edit
        else:
            form = StudentForm(instance=student)
        return render(request, 'schedule/editstudent.html', {'form': form})
    else:
        # Handle unauthorized access (e.g., redirect back to student homepage)
        return redirect('home')
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