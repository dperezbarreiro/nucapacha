# Generated by Django 2.0.4 on 2018-05-17 20:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '0002_auto_20180517_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terms',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='terms',
            name='text_es',
            field=ckeditor.fields.RichTextField(verbose_name='Texto'),
        ),
    ]
