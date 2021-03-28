from django import forms
from .models import Employee


class LoginForm(forms.Form):
    username = forms.CharField(label='Username ', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password ', widget=forms.PasswordInput(attrs={'class': 'form-control icon-password', 'placeholder': 'Password'}))


class EmployeeForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = ['username', 'password', 'name', 'mobile', 'designation']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
        }
