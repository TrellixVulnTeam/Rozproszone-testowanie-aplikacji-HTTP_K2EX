# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20170511_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='redirection_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]