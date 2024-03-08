# forms.py
from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'

class CourseForm(forms.ModelForm): 
    class Meta:
        model = courses
        fields = '__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model = units
        fields = '__all__'

class SpecialEventForm(forms.ModelForm):
    class Meta:
        model = special_events
        fields = '__all__'

class TimetableForm(forms.ModelForm):
    class Meta:
        model = timetable
        fields = '__all__'
