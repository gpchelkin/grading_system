# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161209_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='all_subjects',
            field=models.ManyToManyField(to='core.Subject', verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u044b'),
        ),
    ]