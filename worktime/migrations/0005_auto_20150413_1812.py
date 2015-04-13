# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0004_invent_worktype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invent',
            name='posted_date',
            field=models.DateField(verbose_name='Data dodania'),
        ),
    ]
