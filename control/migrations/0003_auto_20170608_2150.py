# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-08 21:50
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_strip_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strip',
            name='board',
        ),
        migrations.AddField(
            model_name='strip',
            name='color_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
