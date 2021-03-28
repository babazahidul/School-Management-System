from django import forms
from .models import StuShiftInfo, StuClassInfo, StuDetailsInfo
from .models import Student


class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mother_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    roll = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    stu_class = forms.ModelChoiceField(queryset=StuClassInfo.objects.all(), empty_label="Select Class", widget=forms.Select(attrs={'class':'form-control'}))
    stu_shift = forms.ModelChoiceField(queryset=StuShiftInfo.objects.all(), empty_label="Select Shift", widget=forms.Select(attrs={'class':'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    gender_choices=(
        (0,'Male'),
        (1,'Female'),
        (3,'Others'),
    )
    gender = forms.ChoiceField(choices=gender_choices,widget=forms.Select(attrs={'class':'form-control'}))
    stu_section = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    stu_session = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'datePicker'}),
        }


class StudentDetailsModelForm(forms.ModelForm):
    class Meta:
        model = StuDetailsInfo
        exclude = ['student']


class StuSearchForm(forms.Form):
    stu_class = forms.ModelChoiceField(queryset=StuClassInfo.objects.all())
    stu_roll = forms.IntegerField(required=False)
    stu_session = forms.IntegerField(required=False)



