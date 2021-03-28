from django.contrib import admin
from .models import NID, DrivingLicence
# Register your models here.


class DrivingLicenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'l_num']


admin.site.register(NID)
admin.site.register(DrivingLicence, DrivingLicenceAdmin)