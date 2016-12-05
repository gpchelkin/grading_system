# coding=utf-8
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


TYPE_CHOICES = (
    (u'Лекции', u'Лекции'),
    (u'Семинары', u'Семинары'),
    (u'Консультации', u'Консультации'),
    (u'Лабораторные', u'Лабораторные'),
    (u'Контрольно-проверочные мероприятия', u'Контрольно-проверочные мероприятия')
)


class ClassesType(models.Model):
    classes_type = models.CharField(verbose_name="Тип занятий", choices=TYPE_CHOICES, max_length=40)

    def __unicode__(self):
        return u'{}'.format(self.classes_type)