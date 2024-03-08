# forms.py
from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
