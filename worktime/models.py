from django.db import models

# Create your models here.




class Project(models.Model):
    name = models.CharField('Nazwa', max_length=250)
    idname = models.IntegerField('Numer')
    def __str__(self):
        return "{name} {idname}".format(name=self.name, idname=self.idname)


class Employee(models.Model):
    firstName = models.CharField('imie',max_length=25)
    lastName = models.CharField('nazwisko',max_length=25)
    emaliadress = models.EmailField()

    def __str__(self):
        return "{fname} {lname}".format(fname=self.firstName, lname=self.lastName)


class Invent(models.Model):
    project =models.ManyToManyField(Project)
    employee = models.ManyToManyField(Employee)
    posted_date = models.DateTimeField('Data dodania')