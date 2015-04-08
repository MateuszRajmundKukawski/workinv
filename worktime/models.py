from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    emaliadress = models.EmailField()



class Project(models.Model):
    name = models.CharField(max_length=250)
    idname = models.IntegerField()
