# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_damage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='damage',
            field=models.IntegerField(null=True, verbose_name='Preju\xedzo'),
        ),
    ]
