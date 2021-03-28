from django.urls import path
from . import views


urlpatterns = [

    path('attendance/', views.attendance_by_class, name="class-attendance"),
    path('attendance/<stu_class>/<stu_roll>', views.attendance, name="student-attendance")
]
