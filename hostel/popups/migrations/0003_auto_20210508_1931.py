# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-08 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popups', '0002_auto_20210508_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='popup',
            old_name='visible_to',
            new_name='visible_until',
        ),
    ]
