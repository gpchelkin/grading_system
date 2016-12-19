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
    who_rated = models.OneToOneField(verbose_name=u'Кто оценил', to=User)
    type_rated = models.CharField(verbose_name=u'Тип оценившего', default='s', max_length=2, choices=RATED_TYPE)


class TeacherMark(Mark):
    speaker_points = models.IntegerField(verbose_name=u'Ораторские способности', validators=[MaxValueValidator(10), MinValueValidator(1)])
    professionalism_points = models.IntegerField(verbose_name=u'Профессионализм', validators=[MaxValueValidator(10), MinValueValidator(1)])
    exactingness_points = models.IntegerField(verbose_name=u'Требовательность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    understanding_points = models.IntegerField(verbose_name=u'Взаимопонимание', validators=[MaxValueValidator(10), MinValueValidator(1)])
    charisma_points = models.IntegerField(verbose_name=u'Харизматичность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    collective_points = models.IntegerField(verbose_name=u'Атмосфера коллектива', validators=[MaxValueValidator(10), MinValueValidator(1)])
    mark = models.ForeignKey(verbose_name=u'Какой преподаватель', to=Teacher)

    def __unicode__(self):
        return u'Преподаватель: {} Оценки: {}-{}-{}-{}-{}-{}'.format(
            self.mark, self.speaker_points, self.professionalism_points, self.exactingness_points,
            self.understanding_points, self.charisma_points, self.collective_points
        )


class StudentMark(Mark):
    teamwork_points = models.IntegerField(verbose_name=u'Работа в команде', validators=[MaxValueValidator(10), MinValueValidator(1)])
    mutual_points = models.IntegerField(verbose_name=u'Взаимовыручка', validators=[MaxValueValidator(10), MinValueValidator(1)])
    speak_points = models.IntegerField(verbose_name=u'Общительность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    learning_attitudes_points = models.IntegerField(verbose_name=u'Отношение к учебе', validators=[MaxValueValidator(10), MinValueValidator(1)])
    mark = models.ForeignKey(verbose_name=u'Какой студент', to=Student)

    def __unicode__(self):
        return u'Студент: {} Оценки: {}-{}-{}-{}'.format(self.mark, self.teamwork_points, self.mutual_points, self.speak_points, self. learning_attitudes_points)


class SubjectMark(Mark):
    relevance_points = models.IntegerField(verbose_name=u'Актуальность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    availability_points = models.IntegerField(verbose_name=u'Доступность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    thrill_points = models.IntegerField(verbose_name=u'Увлекательность', validators=[MaxValueValidator(10), MinValueValidator(1)])
    fixation_material_points = models.IntegerField(verbose_name=u'Закрепление материала', validators=[MaxValueValidator(10), MinValueValidator(1)])
    learning_material_points = models.IntegerField(verbose_name=u'Методические материалы', validators=[MaxValueValidator(10), MinValueValidator(1)])
    learning_organization_points = models.IntegerField(verbose_name=u'Организация занятий', validators=[MaxValueValidator(10), MinValueValidator(1)])
    what_subject = models.ForeignKey(verbose_name=u'Какой предмет', to=Subject)

    def __unicode__(self):
        return u'Предмет: {} Оценки: {}-{}-{}-{}-{}-{} '.format(
            self.what_subject.name, self.relevance_points, self.availability_points, self.thrill_points,
            self.fixation_material_points, self.learning_material_points, self.learning_organization_points
        )


class NPDMark(Mark):
    difficult_points = models.IntegerField(verbose_name=u'Уровень сложности', validators=[MaxValueValidator(10), MinValueValidator(1)])
    what_npd = models.ForeignKey(verbose_name=u'НПД', to=NPD)

    def __unicode__(self):
        return u'НПД: {} Оценка: {}'.format(self.what_npd.name, self.difficult_points)