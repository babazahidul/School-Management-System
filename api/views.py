from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ResultSerialiver, StudentRegiSerializer
from student.models import Result, Student
from .forms import GetClassForm
from student.models import StuDetailsInfo, Attendance


class StudentInfoview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students_obj= Student.objects.all()
        srializer_obj=StudentRegiSerializer(students_obj, many=True)
        print("Student",students_obj)
        return Response({'status': srializer_obj.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = StudentRegiSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            print("SERIALIZER: ",serializers)
            return Response({'status':'Data save successfullyyyyyyyyy'}, status=status.HTTP_200_OK)
        else:
            return Response({'status Checkkkk': serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


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


class StudentAttendance(APIView):
    def get(self, request, stu_class, stu_roll):
        try:
            Attendance.objects.create_attendance(stu_class, stu_roll)
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as err:
            print("Errors: ", err)
            return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)


class ResultView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print("REQUEST", request)
        print("REQUEST PRINT", request.data)
        serializers = ResultSerialiver(data=request.data)
        if serializers.is_valid():
            board = serializers.validated_data['board']
            roll = serializers.validated_data['roll']
            std_obj = Result.objects.get(board=board, roll=roll)
            print(F"BOARD {board} ROLL {roll}")
            return Response({'result': std_obj.gpa}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)