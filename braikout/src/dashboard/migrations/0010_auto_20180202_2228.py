# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-02 22:28
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_coinprices_predictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinprices',
            name='predictions',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=None),
        ),
    ]
