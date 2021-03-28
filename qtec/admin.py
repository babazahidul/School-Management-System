from django.contrib import admin
from .models import QtechKeywordSearch
# Register your models here.


class QtechSearchAdmin(admin.ModelAdmin):
    list_display =['user', 'search_keyword', 'search_time']

admin.site.register(QtechKeywordSearch, QtechSearchAdmin)