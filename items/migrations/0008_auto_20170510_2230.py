# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-10 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_item_teleport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='teleport',
            field=models.IntegerField(blank=True, null=True, verbose_name='Teleport'),
        ),
    ]
