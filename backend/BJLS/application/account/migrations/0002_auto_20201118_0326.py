# Generated by Django 2.2.13 on 2020-11-18 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_teacher',
            new_name='is_faculty',
        ),
    ]