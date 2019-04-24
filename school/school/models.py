from __future__ import unicode_literals
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=40)
    website = models.URLField()

class Student(models.Model):
    name = models.CharField(max_length=40)

class Subject(models.Model):
    name = models.CharField(max_length=140)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)