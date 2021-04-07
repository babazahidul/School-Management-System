from django.shortcuts import render, redirect
from .models import *
from .forms import StudentForm, StuSearchForm, StudentModelForm, StudentDetailsModelForm
from django.contrib import messages
# Create your views here.


def stu_search(request):
    forms = StuSearchForm()
    stu_class = request.GET.get('stu_class', None)
    stu_roll = request.GET.get('stu_roll', None)
    stu_session = request.GET.get('stu_session', None)
    if stu_class:
        # students = StuDetailsInfo.objects.filter(stu_class__id=stu_class)
        # print("Student: ", students)
        # if stu_roll:
        #     students = students.filter(student__roll=stu_roll)
        #     print("Roll: ", students)
        # if stu_session:
        #     students = students.filter(stu_session=stu_session)
        #     print("Session: ", students)
        students = StuDetailsInfo.objects.filter(stu_class=stu_class)
        if stu_roll:
            students = students.filter(roll=stu_roll)
        if stu_session:
            students = students.filter(stu_session=stu_session)
            messages.success(request, "Get student")
        context = {
            'forms': forms,
            'students': students
        }
        return render(request, 'student/search.html', context)
    context = {
        'forms': forms
    }
    return render(request, 'student/search.html', context)


def student(request):
    if request.method == 'GET':
        forms = StudentForm()
    else:
        forms = StudentForm(request.POST, request.FILES)
        if forms.is_valid():
            name = forms.cleaned_data["name"]
            father_name = forms.cleaned_data['father_name']
            mother_name = forms.cleaned_data['mother_name']
            address = forms.cleaned_data['address']
            roll = forms.cleaned_data['roll']
            stu_class = forms.cleaned_data['stu_class']
            stu_shift = forms.cleaned_data['stu_shift']
            age = forms.cleaned_data['age']
            dob = forms.cleaned_data['dob']
            gender = forms.cleaned_data['gender']
            stu_section = forms.cleaned_data['stu_section']
            stu_session = forms.cleaned_data['stu_session']
            image = forms.cleaned_data['image']
            try:
                stu_create = Student.objects.create(
                    name=name,
                    father_name=father_name,
                    mother_name=mother_name,
                    address=address,
                    age=age,
                    dob=dob,
                    gender=gender,
                    image=image
                )
                StuDetailsInfo.objects.create(
                    student=stu_create,
                    roll=roll,
                    stu_class=stu_class,
                    stu_shift=stu_shift,
                    stu_section=stu_section,
                    stu_session=stu_session,
                )
                messages.success(request, "Student Create Successfully.")
                return redirect('student')

            except:
                messages.warning(request, "This student already exist.")
                return redirect('student')

    context = {
        'forms': forms
    }
    return render(request, 'student/student.html', context)


def stu_register(request):
    if request.method == 'GET':
        forms1 = StudentModelForm()
        forms2 = StudentDetailsModelForm()
    else:
        forms1 = StudentModelForm(request.POST, request.FILES)
        forms2 = StudentDetailsModelForm(request.POST)
        if forms1.is_valid() and forms2.is_valid():
            stu_obj = forms1.save()
            stu_details_obj = forms2.save(commit=False)
            stu_details_obj.student = stu_obj
            stu_details_obj.save()
            messages.success(request,  "Student Registration Successfully.")
            return redirect('home')
    context = {
        'forms1': forms1,
        'forms2': forms2
    }
    return render(request, 'student/registration.html', context)


def student_list(request):
    # student_obj = Student.objects.all()
    stu_obj = StuDetailsInfo.objects.select_related('student', 'stu_class').order_by('-id')

    context = {
        # 'student': student_obj,
        'student_details_obj': stu_obj,
    }
    return render(request, 'student/student_list.html', context)


def edit_student(request, student_id):
    student_obj = Student.objects.get(id=student_id)
    stu_details_obj = StuDetailsInfo.objects.get(student=student_obj)
    forms1 = StudentModelForm(instance = student_obj)
    forms2 = StudentDetailsModelForm(instance = stu_details_obj)
    try:
        if request.method == 'POST':
            forms1 = StudentModelForm(request.POST, instance=student_obj)
            forms2 = StudentDetailsModelForm(request.POST, instance=stu_details_obj)
            if forms1.is_valid() and forms2.is_valid():
                stu_obj = forms1.save()
                stu_details_obj = forms2.save(commit=False)
                stu_details_obj.student = stu_obj
                stu_details_obj.save()
                return redirect('student-list')
    except Exception as err:
        print("Errors: ", err)
    context = {
        'forms1': forms1,
        'forms2': forms2,
    }
    return render(request, 'student/edit_student.html', context)


def del_student(request, student_id):
    student_obj = Student.objects.get(id=student_id)
    student_obj.delete()
    return redirect('student-list')



