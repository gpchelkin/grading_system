# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('npd', '0002_npd_who'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npd',
            name='who',
        ),
    ]
