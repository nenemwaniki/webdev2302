from django.db import models

class units(models.Model):
    unit_code = models.CharField(max_length=10)
    unit_name = models.CharField(max_length=100)
    unit_description = models.TextField()
    unit_lecturer = models.CharField(max_length=100)
    unit_semester = models.IntegerField()
    unit_venue = models.CharField(max_length=100)
    unit_time = models.TimeField()
    

    def __str__(self):
        return self.unit_name
    
class courses(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    course_units = models.ManyToManyField(units)
    
    def __str__(self):
        return self.course_name
    
class students(models.Model):
    student_reg = models.CharField(max_length=10)
    student_name = models.CharField(max_length=100)
    student_course = models.ForeignKey(courses, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.student_name

class timetable(models.Model):
    unit = models.ForeignKey(units, on_delete=models.CASCADE)

    student = models.ForeignKey(students, on_delete=models.CASCADE)
    course= models.ForeignKey(courses, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.unit.unit_name
    
class administrator(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.admin_name

class special_events(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    event_venue = models.CharField(max_length=100)
    
    def __str__(self):
        return self.event_name
