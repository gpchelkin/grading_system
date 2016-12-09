# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 06:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marks', '0002_npdmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='who_rated',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041a\u0442\u043e \u043e\u0446\u0435\u043d\u0438\u043b'),
            preserve_default=False,
        ),
    ]
