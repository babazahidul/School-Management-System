from django import forms
from .models import NID, DrivingLicence


class LicenceForm(forms.ModelForm):
    nid_num = forms.CharField()

    class Meta:
        model = DrivingLicence
        exclude = ('nid',)


class SearchLicenceForm(forms.Form):
    licence_number = forms.CharField()