# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0004_auto_20160911_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='directors',
            field=models.ManyToManyField(related_name='DirectorsRelated', to='mt.Person'),
        ),
        migrations.AddField(
            model_name='asset',
            name='features',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='asset',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='sales_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='actors',
            field=models.ManyToManyField(related_name='ActorsRelated', to='mt.Person'),
        ),
        migrations.AddField(
            model_name='asset',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mt.Genre'),
        ),
    ]
