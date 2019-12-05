# Generated by Django 2.2.5 on 2019-11-17 20:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resorts',
            fields=[
                ('resort_name', models.CharField(max_length=200)),
                ('resort_id', models.IntegerField(primary_key=True, serialize=False)),
                ('beginner', models.FloatField()),
                ('intermediate', models.FloatField()),
                ('expert', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('input_beginner', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('input_intermediate', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('input_expert', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('best_resort', models.CharField(max_length=200)),
                ('resort_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input.Resorts')),
            ],
        ),
    ]
