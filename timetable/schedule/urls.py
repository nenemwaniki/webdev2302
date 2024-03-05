from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("edit/<int:student_id>/", views.edit, name="edit"),
    path('delete/<int:student_id>/', views.delete, name='delete'),

]
