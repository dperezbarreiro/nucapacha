# Generated by Django 2.0.4 on 2018-05-04 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Room & Price', 'verbose_name_plural': 'Rooms & Prices'},
        ),
        migrations.AlterModelOptions(
            name='roomsdescription',
            options={'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
    ]