# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-09 20:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_auto_20180507_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateField(default=datetime.date(2018, 5, 10)),
        ),
    ]