# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0006_auto_20150413_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invent',
            name='employee',
        ),
        migrations.AddField(
            model_name='invent',
            name='employee',
            field=models.ForeignKey(to='worktime.Employee', null=True),
        ),
    ]
