from django.shortcuts import render, get_object_or_404,redirect
import pandas as pd
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    students_list = Students.objects.all()  
    return render(request, 'schedule/index.html', {'students': students_list})

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