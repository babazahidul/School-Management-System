from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, EmployeeForm

# Create your views here.


def employee(request):
    if request.method == 'GET':
        forms = EmployeeForm()

    else:
        forms = EmployeeForm(request.POST)
        if forms.is_valid():
            user_name = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user_create = User.objects.create_user(username=user_name, password=password)
            new_0bj = forms.save(commit=False)
            new_0bj.usern = user_create
            new_0bj.save()
            messages.success(request, 'Employee Create Successfully!')
            return redirect('home')
    context = {
        'forms': forms
    }
    return render(request, 'employee/employee_create.html', context)


def user_login(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                print("Opsss")
    else:
        forms = LoginForm()
    context = {
        'forms': forms
    }
    return render(request, 'admin/user_login.html',context)


def user_logout(request):
    logout(request)
    return redirect('user-login')