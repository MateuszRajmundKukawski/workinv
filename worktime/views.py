from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Invent, Employee
from .forms import InventForm, EmployeeForm

# Create your views here.
class InventListView(ListView):
    model = Invent

# class InventDetailView(DetailView):
#     model = Invent


class InventFormView(FormView):
    form_class = InventForm
    template_name = 'invent_form.html'
    success_url = '/invent'
    def form_invalid(self, form):
        form.save()
        return super(InventFormView, self).form_invalid(form)



class EmploeeyFormView(FormView):
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = '/pracownicy'
    def form_invalid(self, form):
        form.save()
        return super(EmploeeyFormView, self).form_invalid(form)

class EmployeeView(ListView):
    model = Employee

