from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('registration/', views.stu_register, name='student-registration'),
    path('list/', views.student_list, name='student-list'),
    path('search/', views.stu_search, name='student-search'),
    path('edit/<int:student_id>', views.edit_student, name='edit-student'),
    path('delete/<int:student_id>', views.del_student, name='del-student'),
]