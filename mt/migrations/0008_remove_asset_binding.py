# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0007_remove_asset_asin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='binding',
        ),
    ]