# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 18:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0003_mark_who_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0446\u0435\u043d\u0438\u0432\u0430\u043d\u0438\u044f'),
        ),
    ]
