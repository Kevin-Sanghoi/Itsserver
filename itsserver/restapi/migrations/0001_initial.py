# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('plots', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('area', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('wells', models.IntegerField()),
                ('godowns', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('dob', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('plots', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('area', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('wells', models.IntegerField()),
                ('godowns', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('dob', models.DateField(max_length=100)),
            ],
        ),
    ]
