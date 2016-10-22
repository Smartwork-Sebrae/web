# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='history',
            name='order_desk',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='history', to='order.OrderDesk'),
            preserve_default=False,
        ),
    ]