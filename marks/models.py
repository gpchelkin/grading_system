# coding=utf-8
import datetime
from django.db import models

from core.models import Teacher, Student, Subject


class Mark(models.Model):
    date = models.DateTimeField(verbose_name='Дата оценивания', default=datetime.datetime.now())


class TeacherMark(Mark):
    mark = models.ForeignKey(Teacher)


class StudentMark(Mark):
    mark = models.ForeignKey(Student)


class SubjectMark(Mark):
    mark = models.ForeignKey(Subject)
