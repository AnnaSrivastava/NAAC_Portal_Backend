# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_details', '0010_auto_20171025_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.CharField(max_length=4, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='bookchapters',
            name='isbn',
            field=models.IntegerField(verbose_name='ISBN No.'),
        ),
        migrations.AlterField(
            model_name='bookchapters',
            name='page_no',
            field=models.IntegerField(verbose_name='Page No.'),
        ),
        migrations.AlterField(
            model_name='bookchapters',
            name='year',
            field=models.CharField(max_length=4, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='issn_isbn',
            field=models.IntegerField(verbose_name='ISBN No.'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='year',
            field=models.CharField(max_length=4, verbose_name='Year'),
        ),
    ]