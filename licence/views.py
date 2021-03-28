from django.shortcuts import render
from .forms import LicenceForm, SearchLicenceForm
from .models import NID, DrivingLicence
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.


def licence(request):
    forms = LicenceForm()
    if request.method == 'POST':
        forms = LicenceForm(request.POST)
        if forms.is_valid():
            nid = forms.cleaned_data['nid_num']
            try:
                number = NID.objects.get(nid_number=nid)
                if number:
                    obj = forms.save(commit=False)
                    obj.nid=number
                    obj.save()

                    # DrivingLicence.objects.create(
                    #     nid = number,
                    #     name = forms.cleaned_data['name'],
                    #     l_num = forms.cleaned_data['l_num']
                    # )
                    messages.success(request,"Save successfully")
            except NID.DoesNotExist:
                print("No Data")
                messages.warning(request, "No such data against this NID Number")
    context = {
        'forms': forms
    }
    return render(request, 'licence/licence_create.html', context)


def search_licence(request):
    forms = SearchLicenceForm()
    obj = request.GET.get('licence_number', None)
    print("OBJECT", obj)
    try:
        licence_no=DrivingLicence.objects.get(l_num=obj)
        if licence_no:
            context = {
                'licence_no': licence_no,
                'data': obj
            }
            messages.success(request, "Data exist.")
            return render(request, 'licence/search.html', context)

    except DrivingLicence.DoesNotExist:
        if obj:
            messages.warning(request, f"No such data like {obj}")
    context = {
        'forms': forms
    }
    return render(request, 'licence/search.html', context)