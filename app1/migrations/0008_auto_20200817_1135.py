# Generated by Django 3.1 on 2020-08-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_newlicence_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newlicence',
            name='photo',
            field=models.ImageField(upload_to='product/'),
        ),
    ]
