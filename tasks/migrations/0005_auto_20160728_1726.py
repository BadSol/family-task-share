# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20160706_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='delegate',
            new_name='delegates',
        ),
    ]
