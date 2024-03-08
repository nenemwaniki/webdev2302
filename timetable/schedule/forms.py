# forms.py
from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model = Units
        fields = '__all__'

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'

class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = '__all__'

class SpecialEventsForm(forms.ModelForm):
    class Meta:
        model = SpecialEvents
        fields = '__all__'
        
