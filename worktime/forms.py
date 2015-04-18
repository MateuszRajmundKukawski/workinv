from django import forms
from .models import Invent, Employee


class InventForm(forms.ModelForm):
    class Meta:
        model = Invent
        fields = ('project', 'employee', 'posted_date', 'worktype',)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =  ('firstName', 'lastName', 'emaliadress',)

