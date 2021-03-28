from django import forms


class GetClassForm(forms.Form):
    class_name = forms.CharField()