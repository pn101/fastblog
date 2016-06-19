# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
