from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(units)
admin.site.register(courses)
admin.site.register(students)
admin.site.register(timetable)
admin.site.register(admin)
admin.site.register(special_events)

