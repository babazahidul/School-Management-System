from django.urls import path
from rest_framework.authtoken import views as tokenviews
from . import views


urlpatterns = [

    path('attendance/', views.attendance_by_class, name="class-attendance"),
    path('attendance/<stu_class>/<stu_roll>', views.StudentAttendance.as_view(), name="student-attendance"),
    path('result/', views.ResultView.as_view(), name="result"),
    path('student/regi/', views.StudentInfoview.as_view(), name="student-info"),
    path('api-token-auth/', tokenviews.obtain_auth_token)
]
