# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items_produced',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
