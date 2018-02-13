# Generated by Django 2.0.2 on 2018-02-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20180212_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('lvl', 'pk')},
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.IntegerField(choices=[(1, 'Jednoręczne'), (2, 'Dwuręczne'), (3, 'Półtoraręczne'), (4, 'Dystansowe'), (5, 'Pomocnicze'), (6, 'Różdzki'), (7, 'Laski'), (8, 'Zbroje'), (9, 'Hełmy'), (10, 'Buty'), (11, 'Rękawice'), (12, 'Pierścienie'), (13, 'Naszyjniki'), (14, 'Tarcze'), (15, 'Neutralne'), (16, 'Konsumpcyjne'), (17, 'Złoto'), (18, 'Klucze'), (19, 'Questowe'), (20, 'Odnawialne'), (21, 'Strzały'), (22, 'Talizmany'), (23, 'Książki'), (24, 'Torby'), (25, 'Mikstury'), (26, 'Eventowe')], db_index=True, verbose_name='Typ'),
        ),
    ]
