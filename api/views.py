from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import GetClassForm
from student.models import StuDetailsInfo, Attendance


def attendance_by_class(request):
    forms = GetClassForm()
    stu_class = request.GET.get('class_name', None)
    students = StuDetailsInfo.objects.filter(stu_class__class_name=stu_class)
    context = {
        'forms': forms,
        'students': students,
        'stu_class': stu_class
    }
    return render(request, 'student/attendance_by_class.html', context)


@api_view()
def attendance(request, stu_class, stu_roll):
    try:
        Attendance.objects.create_attendance(stu_class, stu_roll)
        context = {
            'status': 'success'
        }
        return Response(context)
    except Exception as err:
        print("Errors: ", err)
        context = {
            'status': 'failed'
        }
        return Response(context)
