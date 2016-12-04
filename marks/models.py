# coding=utf-8
import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import Teacher, Student, Subject


class Mark(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата оценивания', default=datetime.date.today)


class TeacherMark(Mark):
    speaker_points = models.IntegerField(verbose_name=u'Ораторские способности', validators=[MaxValueValidator(10), MinValueValidator(1)])
    professionalism_points = models.IntegerField(verbose_name=u'Профессионализм', validators=[MaxValueValidator(10), MinValueValidator(1)])
    exactingness_points = models.IntegerField(verbose_name=u'Требовательность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    understanding_points = models.IntegerField(verbose_name=u'Взаимопонимание', validators=[MaxValueValidator(10), MinValueValidator(1)])
    charisma_points = models.IntegerField(verbose_name=u'Харизматичность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    collective_points = models.IntegerField(verbose_name=u'Атмосфера коллектива', validators=[MaxValueValidator(10), MinValueValidator(1)])
    mark = models.ForeignKey(Teacher)


class StudentMark(Mark):
    teamwork_points = models.IntegerField(verbose_name=u'Работа в команде', validators=[MaxValueValidator(10), MinValueValidator(1)])
    mutual_points = models.IntegerField(verbose_name=u'Взаимовыручка', validators=[MaxValueValidator(10), MinValueValidator(1)])
    speak_points = models.IntegerField(verbose_name=u'Общительность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    learning_attitudes_points = models.IntegerField(verbose_name=u'Отношение к учебе', validators=[MaxValueValidator(10), MinValueValidator(1)])
    mark = models.ForeignKey(Student)

    def __unicode__(self):
        return u'Студент: {} Оценки: {}-{}-{}-{}'.format(self.mark, self.teamwork_points, self.mutual_points, self.speak_points, self. learning_attitudes_points)


class SubjectMark(Mark):
    relevance_points = models.IntegerField(verbose_name=u'Актуальность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    availability_points = models.IntegerField(verbose_name=u'Доступность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    thrill_points = models.IntegerField(verbose_name=u'Увлекательность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    fixation_material_points = models.IntegerField(verbose_name=u'Закрепление материала', validators=[MaxValueValidator(10), MinValueValidator(1)])
    learning_material_points = models.IntegerField(verbose_name=u'Методические материалы', validators=[MaxValueValidator(10), MinValueValidator(1)])
    learning_organization_points = models.IntegerField(verbose_name=u'Организация занятий', validators=[MaxValueValidator(10), MinValueValidator(1)])
    mark = models.ForeignKey(Subject)
