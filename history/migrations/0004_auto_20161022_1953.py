# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_auto_20161022_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='order_desk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='order.OrderDesk'),
        ),
    ]