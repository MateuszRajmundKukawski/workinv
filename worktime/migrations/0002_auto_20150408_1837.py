# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invent',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('posted_date', models.DateTimeField(verbose_name='Data dodania')),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='firstName',
            field=models.CharField(verbose_name='imie', max_length=25),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lastName',
            field=models.CharField(verbose_name='nazwisko', max_length=25),
        ),
        migrations.AlterField(
            model_name='project',
            name='idname',
            field=models.IntegerField(verbose_name='Numer'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(verbose_name='Nazwa', max_length=250),
        ),
        migrations.AddField(
            model_name='invent',
            name='employee',
            field=models.ManyToManyField(to='worktime.Employee'),
        ),
        migrations.AddField(
            model_name='invent',
            name='project',
            field=models.ManyToManyField(to='worktime.Project'),
        ),
    ]
