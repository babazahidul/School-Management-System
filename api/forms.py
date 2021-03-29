from django import forms


class GetClassForm(forms.Form):
    class_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'label':'form-check-label'}))