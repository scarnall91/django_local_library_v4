# Generated by Django 2.2.5 on 2019-11-17 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0002_auto_20191117_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='best_resort',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='resort',
        ),
    ]
