# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afdguser',
            name='username',
            field=models.CharField(max_length=31, unique=True),
        ),
    ]
