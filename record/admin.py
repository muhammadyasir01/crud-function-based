from django.contrib import admin
from .models import *

class DataBaseAdmin (admin.ModelAdmin):
    list_display = ('id','name', 'designation','section')


admin.site.register(DataBase,DataBaseAdmin)
