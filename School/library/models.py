# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from school_structure.models import School
from students.models import Student

# Create your models here.


class IssueRuleBook(models.Model):
    school = models.ForeignKey(School)
    max_issue_period = models.IntegerField()
    late_submission_fine = models.IntegerField()


class Book(models.Model):
    school = models.ForeignKey(School)
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=70)
    publisher = models.CharField(max_length=70)
    min_age = models.IntegerField()
    min_class = models.IntegerField()
    is_issued = models.BooleanField()
    issued_to = models.ForeignKey(Student)
    issued_on = models.DateField()
    return_date = models.DateField()
    late_return_by_days = models.IntegerField()