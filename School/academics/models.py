# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from school_structure.models import School, SchoolSubject, SchoolClass
# Create your models here.


class AnnualSyllabus(models.Model):
    school = models.ForeignKey(School)
    standard = models.ForeignKey(SchoolClass)
    subject = models.ForeignKey(SchoolSubject)
    total_chapters = models.IntegerField()
    annual_assessment_structure = JSONField()


class AcademicProgress(models.Model):
    school = models.ForeignKey(School)
    standard = models.ForeignKey(SchoolClass)
    progress_json = JSONField()


class HomeworkReport(models.Model):
    school = models.ForeignKey(School)
    standard = models.ForeignKey(SchoolClass)
    date = models.DateField()
    homework = JSONField()

