from django.contrib import admin

# Register your models here.
from .models import Employee, Project, Invent


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'emaliadress')
    search_fields = ['firstName', 'lastName', 'emaliadress']



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'idname')
class InventAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project','worktype', 'posted_date', )



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Invent, InventAdmin)
