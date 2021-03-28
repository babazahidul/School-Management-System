from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher, name='teacher'),
    path('list/', views.teacher_list, name="teacher-list"),
    path('edit/<int:teacher_id>', views.edit_teacher, name='edit-teacher'),
    path('delete/<int:teacher_id>', views.del_teacher, name='del-teacher')
]