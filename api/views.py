from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import GetClassForm
from student.models import StuDetailsInfo, Attendance


def attendance_by_class(request):
    forms = GetClassForm()
    stu_class = request.GET.get('class_name', None)
    students = StuDetailsInfo.objects.filter(stu_class__class_name=stu_class).order_by('roll')
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
        return Response({'status': 'success'}, status=status.HTTP_200_OK )
    except Exception as err:
        print("Errors: ", err)
        return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)
