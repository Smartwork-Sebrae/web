# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Manager', 'verbose_name_plural': 'Managers'},
        ),
        migrations.AlterField(
            model_name='manager',
            name='hour',
            field=models.TimeField(max_length=10, verbose_name='Hora'),
        ),
    ]
