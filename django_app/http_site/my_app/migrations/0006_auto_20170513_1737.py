# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_auto_20170513_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batch_t', to='my_app.Test'),
        ),
    ]
