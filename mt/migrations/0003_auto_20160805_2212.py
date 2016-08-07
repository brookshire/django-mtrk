# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0002_assettransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assettransaction',
            name='trans',
            field=models.IntegerField(choices=[(1, b'In Inventory'), (2, b'Checked Out'), (3, b'Loaned'), (-1, b'Unknown'), (4, b'Removed from Inventory Permanently')], default=1),
        ),
    ]
