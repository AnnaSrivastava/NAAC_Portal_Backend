# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20171109_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dontfill',
            old_name='bookchapters',
            new_name='book_chapters',
        ),
        migrations.RenameField(
            model_name='dontfill',
            old_name='extra_activities',
            new_name='extra',
        ),
        migrations.RenameField(
            model_name='dontfill',
            old_name='guest_lecturer',
            new_name='guest_lecture',
        ),
        migrations.RenameField(
            model_name='dontfill',
            old_name='moab',
            new_name='membership',
        ),
        migrations.RenameField(
            model_name='dontfill',
            old_name='professional_details',
            new_name='professional',
        ),
        migrations.RenameField(
            model_name='dontfill',
            old_name='project',
            new_name='projects',
        ),
    ]
