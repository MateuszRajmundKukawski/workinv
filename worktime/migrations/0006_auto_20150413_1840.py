# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0005_auto_20150413_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invent',
            name='project',
        ),
        migrations.AddField(
            model_name='invent',
            name='project',
            field=models.ForeignKey(null=True, to='worktime.Project'),
        ),
    ]
