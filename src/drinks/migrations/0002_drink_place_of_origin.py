# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-09 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='place_of_origin',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]