# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-09 04:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='date_internship',
            new_name='end_internship',
        ),
    ]
