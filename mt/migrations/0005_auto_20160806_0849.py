# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0004_auto_20160806_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assettransaction',
            name='note',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
