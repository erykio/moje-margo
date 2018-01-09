# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-10 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_item_lowheal2turns'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='resmanaendest_ene',
            field=models.IntegerField(blank=True, null=True, verbose_name='Obniżanie niszczenia energii'),
        ),
        migrations.AddField(
            model_name='item',
            name='resmanaendest_mana',
            field=models.IntegerField(blank=True, null=True, verbose_name='Obniżanie niszczenia many'),
        ),
        migrations.AddField(
            model_name='item',
            name='source_url',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Źródło przedmiotu'),
        ),
        migrations.AlterField(
            model_name='item',
            name='teleport',
            field=models.IntegerField(blank=True, null=True, verbose_name='??? Teleport'),
        ),
    ]
