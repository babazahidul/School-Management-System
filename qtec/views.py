from django.shortcuts import render
from .forms import SearchForm
# Create your views here.


def qtec_problem_0(request):
    if request.method == 'GET':
        forms = SearchForm()
    else:
        forms = SearchForm(request.POST)
        if request.user:
            u = request.user
        else:
            u = None
        if forms.is_valid():

            obj = forms.save(commit=False)
            obj.user = u
            obj.save()
    context = {
        'forms': forms
    }
    return render(request, 'qtec/search.html', context)
