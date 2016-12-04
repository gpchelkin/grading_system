# coding=utf-8
import datetime
from django.db import models

from core.models import Teacher, Student, Subject


class Mark(models.Model):
    date = models.DateTimeField(verbose_name='Дата оценивания', default=datetime.datetime.now())


class TeacherMark(Mark):
    mark = models.ForeignKey(Teacher)

    class Meta:
        verbose_name = 'оценка преподавателя'
        verbose_name_plural = 'оценки преподавателей'


class StudentMark(Mark):
    mark = models.ForeignKey(Student)

    class Meta:
        verbose_name = 'оценка студента'
        verbose_name_plural = 'оценки студентов'


class SubjectMark(Mark):
    mark = models.ForeignKey(Subject)

    class Meta:
        verbose_name = 'оценка предмета'
        verbose_name_plural = 'оценки предметов'
