# Generated by Django 3.1 on 2020-08-14 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formarmodel',
            old_name='distirct',
            new_name='pasword',
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='distirct',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='adminmodel',
            name='photo',
        ),
    ]
