# Generated by Django 3.1 on 2020-08-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_newlicence_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='newlicence',
            name='photo',
            field=models.ImageField(default=False, upload_to='product/'),
        ),
    ]
