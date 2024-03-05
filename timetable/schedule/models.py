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
    
class units(models.Model):
    unit_name = models.CharField(max_length=100)
    unit_code = models.CharField(max_length=100)
    unit_description = models.CharField(max_length=100)
    unit_lecturer = models.CharField(max_length=100)

    def __str__(self):
        return self.unit_name
    
class timetable(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(units, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.student.name + ' - ' + self.unit.unit_name
    
class course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    course_description = models.CharField(max_length=100)
    course_lecturer = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name