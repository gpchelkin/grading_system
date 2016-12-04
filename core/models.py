# coding=utf-8
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


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
    pass


class Student(models.Model):
    semester = models.CharField(verbose_name='Семестр обучения', choices=SEMESTER_CHOICES, default='1', max_length=5)
    year_start = models.IntegerField(verbose_name='Год поступления', validators=[MaxValueValidator(3000), MinValueValidator(1970)])
    year_end = models.IntegerField(verbose_name='Год окончания', validators=[MaxValueValidator(3000), MinValueValidator(1970)])
    course = models.CharField(verbose_name='Курс', choices=COURSE_CHOICE, default='1', max_length=5)
    user_connection = models.OneToOneField(User)

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'


class Teacher(models.Model):
    user_connection = models.OneToOneField(User)

    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'


class Subject(models.Model):
    name = models.CharField(verbose_name='Предмет', max_length=50)
    semester = models.CharField(verbose_name='Семестр обучения', choices=SEMESTER_CHOICES, default='1', max_length=5)
    course = models.CharField(verbose_name='Курс', choices=COURSE_CHOICE, default='1', max_length=5)

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'