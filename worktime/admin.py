from django.contrib import admin

# Register your models here.
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'emaliadress')



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'idname')
class InventAdmin(admin.ModelAdmin):
    list_display = ('posted_date',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Invent, InventAdmin)