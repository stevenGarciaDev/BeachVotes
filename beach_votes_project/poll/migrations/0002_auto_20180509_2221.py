# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-09 22:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='date_of_vote',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
