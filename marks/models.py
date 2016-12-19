# coding=utf-8
import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import Teacher, Student, Subject, User
from npd.models import NPD

RATED_TYPE = (
    ('t', u'Преподаватель'),
    ('s', u'Студент'),
    ('a', u'Администратор'),
    ('p', u'Предмет'),
    ('n', u'НПД')
)


class Scale(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата заведения', default=datetime.datetime.now)
    name = models.TextField(verbose_name=u'Наименование шкалы', default='Default scale')
    max_value = models.IntegerField(verbose_name=u'Максимальное значение', default=10)
    min_value = models.IntegerField(verbose_name=u'Минимальное значение', default=1)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Krit(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата заведения', default=datetime.datetime.now)
    name = models.TextField(verbose_name=u'Наименование критерия', default='Default name')
    scale = models.ForeignKey(verbose_name=u'Шкала', to=Scale)
    type = models.CharField(verbose_name=u'Оцениваемая сущность', default='p', max_length=2, choices=RATED_TYPE)

    def __unicode__(self):
        return u'Критерий {}'.format(self.name)


class Mark(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата оценивания', default=datetime.datetime.now)
    type_rated = models.CharField(verbose_name=u'Тип оценившего', default='s', max_length=2, choices=RATED_TYPE)
    user_rated = models.ForeignKey(User, null=True, related_name='user_that_rated')
    type_marked = models.CharField(verbose_name=u'Тип оцениваемого', default='s', max_length=2, choices=RATED_TYPE)
    user_marked = models.ForeignKey(verbose_name=u'Кого оцениваем', to=User, related_name='user_whom_marked', null=True, blank=True)
    subject_marked = models.ForeignKey(verbose_name=u'Оцениваемый предмет', to=Subject, null=True, blank=True)
    mark_value = models.IntegerField(verbose_name=u'Оценка', default='1')
    criterion = models.ForeignKey(verbose_name=u'Критерий', to=Krit, null=True)

    def __unicode__(self):
        return u'Оценка типа {}, оценил {}'.format(self.type_rated, self.type_marked)
