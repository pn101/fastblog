# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_is_phonenumber_exists'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='signup_slack_notification',
            field=models.BooleanField(default=False),
        ),
    ]
