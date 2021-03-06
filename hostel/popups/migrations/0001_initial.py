# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-08 19:26
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=1024)),
                ('html', ckeditor.fields.RichTextField()),
                ('html_es', ckeditor.fields.RichTextField()),
                ('visible_from', models.DateTimeField(null=True)),
                ('visible_to', models.DateTimeField(null=True)),
                ('display_options', models.CharField(choices=[('once', 'Once'), ('daily', 'Daily'), ('always', 'Always')], default='daily', max_length=255)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Popup',
                'verbose_name_plural': 'Popups',
            },
        ),
    ]
