# Generated by Django 2.2.13 on 2021-02-09 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210119_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='takenClass',
        ),
    ]