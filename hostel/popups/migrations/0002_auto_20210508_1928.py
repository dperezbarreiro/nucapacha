# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-08 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popup',
            name='visible_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='popup',
            name='visible_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
