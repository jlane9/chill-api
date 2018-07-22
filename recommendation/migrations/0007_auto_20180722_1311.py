# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-22 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0006_auto_20180722_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historylistshow',
            name='episode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Episode', verbose_name=b'Episode watched'),
        ),
    ]
