from django import forms
from .models import QtechKeywordSearch


class SearchForm(forms.ModelForm):
    class Meta:
        model = QtechKeywordSearch
        exclude = ('user', 'search_time')
        widgets = {
            'search_keyword': forms.TextInput(attrs={'class': 'form-control'})
        }