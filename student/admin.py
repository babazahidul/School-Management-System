from django.contrib import admin
from .models import *
# Register your models here


class StuDetailsInfoAdmin(admin.ModelAdmin):
    list_display = ['student', 'roll', 'stu_class', 'stu_shift', 'stu_section' ,'stu_session']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'image']


admin.site.register(Student, StudentAdmin)
admin.site.register(StuClassInfo)
admin.site.register(StuShiftInfo)
admin.site.register(Attendance)
admin.site.register(StuDetailsInfo, StuDetailsInfoAdmin)