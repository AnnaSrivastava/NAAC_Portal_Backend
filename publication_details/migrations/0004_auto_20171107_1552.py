# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_details', '0003_auto_20171107_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalpapers',
            name='hindex',
            field=models.IntegerField(default=12, verbose_name=b'H-Index of Journal using Scimago (if Scopus, SCI-Ex or SCI)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='journalpapers',
            name='impact_factor',
            field=models.IntegerField(default=12, verbose_name=b'Impact Factor if SCI-Ex or SCI'),
            preserve_default=False,
        ),
    ]
