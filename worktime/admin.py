from django.contrib import admin

# Register your models here.
from worktime.models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'emaliadress')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'idname')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)