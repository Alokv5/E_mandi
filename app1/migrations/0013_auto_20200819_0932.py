# Generated by Django 3.1 on 2020-08-19 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_viewlicense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewlicense',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
