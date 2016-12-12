# coding=utf-8
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from curriculum.models import ClassesType

SEMESTER_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
)

COURSE_CHOICE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)


class User(AbstractUser):
    is_student = models.BooleanField("Этот пользователь студент", default=False)
    is_teacher = models.BooleanField("Этот пользователь учитель", default=False)


class Group(models.Model):
    name = models.CharField(verbose_name=u'Группа', max_length=10)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Student(models.Model):
    year_start = models.IntegerField(verbose_name=u'Год поступления', validators=[MaxValueValidator(3000), MinValueValidator(1970)])
    year_end = models.IntegerField(verbose_name=u'Год окончания', validators=[MaxValueValidator(3000), MinValueValidator(1970)])
    user_group_full_name = models.ForeignKey(verbose_name=u'Группа студента', to=Group)
    user_connection = models.OneToOneField(verbose_name=u'Пользователь', to=User)

    def __unicode__(self):
        return u'{} {}'.format(self.user_connection.first_name, self.user_connection.last_name)


class Subject(models.Model):
    name = models.CharField(verbose_name=u'Предмет', max_length=50)
    subject_group = models.ManyToManyField(verbose_name=u'Группы', to=Group)
    subject_type = models.ForeignKey(verbose_name=u'Тип предмета', to=ClassesType)

    def __unicode__(self):
        return u'{} - {}'.format(self.name, self.subject_type)


class Teacher(models.Model):
    all_subjects = models.ManyToManyField(verbose_name=u'Предметы', to=Subject)
    user_connection = models.OneToOneField(User)

    def __unicode__(self):
        return u'{} {}'.format(self.user_connection.first_name, self.user_connection.last_name)
