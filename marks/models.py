# coding=utf-8
import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import Teacher, Student, Subject, User
from npd.models import NPD

RATED_TYPE = (
    ('t', u'Преподаватель'),
    ('s', u'Студент'),
    ('a', u'Администратор')
)


class Mark(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата оценивания', default=datetime.datetime.now)
    type_rated = models.CharField(verbose_name=u'Тип оценившего', default='s', max_length=2, choices=RATED_TYPE)


