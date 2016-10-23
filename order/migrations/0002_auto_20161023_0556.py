# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='desks',
            field=models.ManyToManyField(blank=True, related_name='orders', through='order.OrderDesk', to='desk.Desk', verbose_name='Esta\xe7\xf5es de Trabalho'),
        ),
    ]
