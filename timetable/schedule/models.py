from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
