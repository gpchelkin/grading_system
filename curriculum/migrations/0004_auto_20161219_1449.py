# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_auto_20161209_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classestype',
            options={'verbose_name': '\u0422\u0438\u043f \u0437\u0430\u043d\u044f\u0442\u0438\u044f', 'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0437\u0430\u043d\u044f\u0442\u0438\u0439'},
        ),
        migrations.AlterField(
            model_name='classestype',
            name='classes_type',
            field=models.CharField(choices=[('\u041b\u0435\u043a\u0446\u0438\u0438', '\u041b\u0435\u043a\u0446\u0438\u0438'), ('\u0421\u0435\u043c\u0438\u043d\u0430\u0440\u044b', '\u0421\u0435\u043c\u0438\u043d\u0430\u0440\u044b'), ('\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u0438', '\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u0438'), ('\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0435', '\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0435'), ('\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u043e-\u043f\u0440\u043e\u0432\u0435\u0440\u043e\u0447\u043d\u044b\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f', '\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u043e-\u043f\u0440\u043e\u0432\u0435\u0440\u043e\u0447\u043d\u044b\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f')], max_length=40, verbose_name='\u0422\u0438\u043f \u0437\u0430\u043d\u044f\u0442\u0438\u0439'),
        ),
    ]
