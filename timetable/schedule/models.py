from django.db import models

class Units(models.Model):  # Use PascalCase for model names
    code = models.CharField(max_length=10, unique=True)  # Ensure unique unit codes
    name = models.CharField(max_length=100)
    description = models.TextField( blank=True)
    lecturer = models.CharField(max_length=100)
    semester = models.FloatField()
    venue = models.CharField(max_length=100, blank=True)
    time = models.TimeField( blank=True)

    def __str__(self):
        return self.name

class Courses(models.Model):  # Use PascalCase for model names
    code = models.CharField(max_length=10, unique=True)  # Ensure unique course codes
    name = models.CharField(max_length=100)
    description = models.TextField()
    units = models.ManyToManyField(Units, related_name='courses', blank=True)  # Specify related_name

    def __str__(self):
        return self.name

class Students(models.Model):
    reg = models.CharField(max_length=10, unique=True)  # Ensure unique student registration IDs
    name = models.CharField(max_length=100)
    Program = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)


    def __str__(self):
        return self.name

class Timetable(models.Model):
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.unit.name} - {self.student.name}"

class Administrator(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)  # Consider using a password hashing mechanism

    def __str__(self):
        return self.admin_name

class SpecialEvents(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.name
