# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-09 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0008_remove_drinkinfo_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkinfo',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]