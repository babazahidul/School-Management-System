from django.contrib import admin
from .models import Teacher
# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation']
    list_editable = ['designation']


admin.site.register(Teacher, TeacherAdmin)

