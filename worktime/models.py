from django.db import models

# Create your models here.




class Project(models.Model):
    name = models.CharField('Nazwa', max_length=250)
    idname = models.IntegerField('Numer')
    def __str__(self):
        return "{name} nr: {idname}".format(name=self.name, idname=self.idname)


class Employee(models.Model):
    firstName = models.CharField('imie',max_length=25, null=False)
    lastName = models.CharField('nazwisko',max_length=25, null=False)
    emaliadress = models.EmailField(null=False,)

    def __str__(self):
        return "{fname} {lname}".format(fname=self.firstName, lname=self.lastName)


class Invent(models.Model):
    praca = 'PR'
    urlop = 'UR'
    delegacja = 'DL'
    zwolnienie = "ZW"
    WORK_TYPE_CHOICES =(
        (praca,'praca'),
        (urlop,'urlop'),
        (delegacja,'delegacja'),
         (zwolnienie,'zwolnienie'),
    )
    project =models.ForeignKey(Project)
    employee = models.ForeignKey(Employee)
    posted_date = models.DateField('Data dodania')
    worktype = models.CharField(max_length=10, choices=WORK_TYPE_CHOICES, default=praca)

    def __str__(self):
        return "{employee} {project} {worktype} {posted_date}".format(
            employee=self.employee,
            project = self.project.name,
            worktype = self.get_worktype_display(),# get_NAZWAPOLA_display
            posted_date = self.posted_date,
            )
