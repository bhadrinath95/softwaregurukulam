# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-18 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sg_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='startingdate',
            field=models.DateField(blank=True),
        ),
    ]
