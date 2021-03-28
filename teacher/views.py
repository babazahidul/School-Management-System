from django.shortcuts import render, redirect
from .forms import TeacherCreateForm
from .models import Teacher
# Create your views here.


def del_teacher(request, teacher_id):
    teacher_obj = Teacher.objects.get(id=teacher_id)
    teacher_obj.delete()
    return redirect('teacher-list')


def edit_teacher(request, teacher_id):
    teacher_obj = Teacher.objects.get(id=teacher_id)
    forms = TeacherCreateForm(instance=teacher_obj)
    try:
        if request.method == 'POST':
            forms = TeacherCreateForm(request.POST, instance=teacher_obj)
            if forms.is_valid():
                forms.save()
                return redirect('teacher-list')
    except Exception as err:
        print("Errors: ", err)
    context = {
        'forms': forms
    }
    return render(request, 'teacher/edit_teacher.html', context)


def teacher(request):
    forms = TeacherCreateForm()
    try:
        if request.method == 'POST':
            forms = TeacherCreateForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('teacher-list')
    except Exception as err:
        print("Errors: ", err)
    context = {
        'forms': forms
    }
    return render(request, 'teacher/teacher.html', context)


def teacher_list(request):
    teachers_obj = Teacher.objects.all()
    context = {
        'teachers': teachers_obj
    }
    return render(request, 'teacher/teacher_list.html', context)