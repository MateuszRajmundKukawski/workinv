# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0003_remove_employee_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='invent',
            name='worktype',
            field=models.CharField(choices=[('PR', 'praca'), ('UR', 'urlop'), ('DL', 'delegacja'), ('ZW', 'zwolnienie')], max_length=10, default='PR'),
        ),
    ]
