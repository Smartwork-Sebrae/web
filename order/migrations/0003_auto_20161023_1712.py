# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20161023_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('created', 'Criada'), ('started', 'Iniciada'), ('stoped', 'Pausada'), ('finished', 'Terminada')], default='started', max_length=20, verbose_name='Status'),
        ),
    ]
