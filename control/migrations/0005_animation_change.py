# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_strip_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('max_length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('led', models.IntegerField()),
                ('new_color', models.CharField(max_length=6)),
            ],
        ),
    ]