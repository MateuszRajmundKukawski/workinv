# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0007_auto_20150413_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invent',
            name='employee',
            field=models.ForeignKey(to='worktime.Employee'),
        ),
        migrations.AlterField(
            model_name='invent',
            name='project',
            field=models.ForeignKey(to='worktime.Project'),
        ),
    ]
