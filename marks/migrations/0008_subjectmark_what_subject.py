# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20161212_1354'),
        ('marks', '0007_auto_20161214_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectmark',
            name='what_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Subject', verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442'),
            preserve_default=False,
        ),
    ]
