from django.shortcuts import render, get_object_or_404,redirect
import pandas as pd
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    # show student on index page
    students = students.objects.all()
    return render(request, 'schedule/index.html', {'students': students})





