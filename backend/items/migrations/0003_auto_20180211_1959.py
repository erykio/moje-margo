# Generated by Django 2.0.2 on 2018-02-11 19:59
from django.contrib.postgres.operations import UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_reqp'),
    ]

    operations = [
        UnaccentExtension()
    ]
