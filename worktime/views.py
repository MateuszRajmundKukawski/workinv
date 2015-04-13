from django.shortcuts import render
from django.views.generic import ListView
from .models import Invent

# Create your views here.
class InventListView(ListView):
    model = Invent
