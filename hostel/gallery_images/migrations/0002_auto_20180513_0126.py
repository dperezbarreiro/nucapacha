# Generated by Django 2.0.4 on 2018-05-13 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='category',
            field=models.CharField(choices=[('pool-bar', 'Pool&Bar'), ('breakfast', 'Breakfast'), ('tv', 'TV Room'), ('rooms', 'Guest Rooms')], max_length=10),
        ),
    ]
