from django.db import models

class Units(models.Model):  # Use PascalCase for model names
    unit_code = models.CharField(max_length=10, unique=True)  # Ensure unique unit codes
    unit_name = models.CharField(max_length=100)
    unit_description = models.TextField()
    unit_lecturer = models.CharField(max_length=100)
    unit_semester = models.IntegerField()
    unit_venue = models.CharField(max_length=100)
    unit_time = models.TimeField()

    def __str__(self):
        return self.unit_name

class Courses(models.Model):  # Use PascalCase for model names
    course_code = models.CharField(max_length=10, unique=True)  # Ensure unique course codes
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    course_units = models.ManyToManyField(Units, related_name='courses')  # Specify related_name

    def __str__(self):
        return self.course_name

class Students(models.Model):
    student_reg = models.CharField(max_length=10, unique=True)  # Ensure unique student registration IDs
    student_name = models.CharField(max_length=100)
    student_course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.student_name

class Timetable(models.Model):
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.unit.unit_name} - {self.student.student_name}"

class Administrator(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)  # Consider using a password hashing mechanism

    def __str__(self):
        return self.admin_name

class SpecialEvents(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    event_venue = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name
