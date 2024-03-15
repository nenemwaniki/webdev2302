from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Admin URLs (accessible only to superusers)
    path("admin/", admin.site.urls),  # Admin site
    path("", views.index, name="index"),  # Admin view (replace with specific view if needed)

    # Student URLs (accessible to authenticated users)
    path("home/", views.home, name="home"),  # Student landing page
    path("editstudent/<int:pk>/", views.editstudent, name="editstudent"),  # Edit student profile

    # Other URLs (accessible to potentially any user role)
    path('login/', views.login, name='login'),  # Sign-in view 
    path("newstudent/", views.newstudent, name="newstudent"),  # Create new student (admin/staff?)
    path("units/", views.units, name="units"),  # Units list (public/restricted?)
    path("newunit/", views.newunit, name="newunit"),  # Create new unit (admin/staff?)
    path("editunit/<int:pk>/", views.editunit, name="editunit"),  # Edit unit (admin/staff?)
    path("deleteunit/<int:pk>/", views.deleteunit, name="deleteunit"),  # Delete unit (admin/staff?)
    path("courses/", views.courses, name="courses"),  # Courses list (public/restricted?)
    path("editcourse/<int:pk>/", views.editcourse, name="editcourse"),  # Edit course (admin/staff?)
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # Logout view
    path("social-auth/", include("allauth.urls")),  # URL to redirect to after successful login
    path("accounts/", include("allauth.urls")),  # URL to redirect to after successful login
]
