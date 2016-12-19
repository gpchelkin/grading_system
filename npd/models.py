# coding=utf-8
from django.db import models

from core.models import Student

NPD_CHOICE = (
    (u'Научно-исследовательская работа', u'Научно-исследовательская работа'),
    (u'Педагогическая практика', u'Педагогическая практика'),
    (u'Выступление на конференциях', u'Выступление на конференциях'),
    (u'Дипломная работа', u'Дипломная работа'),
    (u'Написание статей', u'Написание статей'),
    (u'Производственная практика', u'Производственная практика'),
    (u'Преддипломная практика', u'Преддипломная практика'),
)


class NPD(models.Model):
    name = models.CharField(verbose_name=u'Научно-практическая деятельность', choices=NPD_CHOICE, max_length=50)

    class Meta:
        verbose_name = u'Научно-практическая деятельность'
        verbose_name_plural = u'Научно-практические деятельности'

    def __unicode__(self):
        return u'{}'.format(self.name)
