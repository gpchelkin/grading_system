# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161209_0934'),
        ('npd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='npd',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student', verbose_name='\u041a\u0442\u043e \u043e\u0446\u0435\u043d\u0438\u0432\u0430\u0435\u0442'),
            preserve_default=False,
        ),
    ]