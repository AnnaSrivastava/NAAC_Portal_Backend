# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0015_workshop_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='role',
            field=models.CharField(max_length=100, verbose_name='Role'),
        ),
    ]