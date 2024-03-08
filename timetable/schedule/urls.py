from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newstudent/", views.newstudent, name="newstudent"),
    path("editstudent/<int:pk>/", views.editstudent, name="editstudent"),
    path("deletestudent/<int:pk>/", views.deletestudent, name="deletestudent"),
    
]
