# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 13:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0006_asset_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='asin',
        ),
    ]
