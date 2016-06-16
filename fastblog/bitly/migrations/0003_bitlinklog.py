# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bitly', '0002_auto_20160616_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='BitLinkLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('http_user_agent', models.CharField(blank=True, max_length=255, null=True)),
                ('http_referer', models.CharField(blank=True, max_length=255, null=True)),
                ('http_remote_addr', models.CharField(blank=True, max_length=31, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bitlink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bitly.BitLink')),
            ],
        ),
    ]
