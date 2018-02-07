# Generated by Django 2.0.2 on 2018-02-07 07:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0020_auto_20170517_1951'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemBonus',
            new_name='ItemLegbon',
        ),
        migrations.AddField(
            model_name='item',
            name='stats',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, verbose_name='Statystyki w kolejności'),
        ),
    ]
