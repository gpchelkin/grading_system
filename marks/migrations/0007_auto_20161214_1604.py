# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0006_auto_20161214_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmark',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041e\u0446\u0435\u043d\u0438\u0432\u0448\u0438\u0439'),
        ),
    ]