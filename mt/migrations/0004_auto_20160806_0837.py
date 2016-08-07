# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0003_auto_20160805_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assettransaction',
            name='trans',
            field=models.IntegerField(choices=[(1, b'In Inventory'), (2, b'Checked Out'), (3, b'Loaned'), (0, b'Unknown'), (4, b'Removed from Inventory Permanently')], default=1),
        ),
    ]
