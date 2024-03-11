from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newstudent/", views.newstudent, name="newstudent"),
    path("editstudent/<int:pk>/", views.editstudent, name="editstudent"),
    path("deletestudent/<int:pk>/", views.deletestudent, name="deletestudent"),
    path("units/", views.units, name="units"),
    path("newunit/", views.newunit, name="newunit"),
    path("editunit/<int:pk>/", views.editunit, name="editunit"),
    path("deleteunit/<int:pk>/", views.deleteunit, name="deleteunit"),
    path("courses/", views.courses, name="courses"),
    path("editcourse/<int:pk>/", views.editcourse, name="editcourse"),    
]
