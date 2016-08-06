# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans', models.CharField(choices=[(b'add', b'In Inventory'), (b'co', b'Checked Out'), (b'col', b'Loaned'), (b'unk', b'Unknown'), (b'rem', b'Removed from Inventory Permanently')], default=b'add', max_length=3)),
                ('note', models.CharField(blank=True, max_length=256)),
                ('ts', models.DateTimeField(auto_now_add=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mt.MovieAsset')),
            ],
        ),
    ]
