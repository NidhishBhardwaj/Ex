# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from school_structure.models import School

# Create your models here.


class VisitorRecord(models.Model):
    school = models.ForeignKey(School)
    date = models.DateTimeField()
    visitor_name = models.CharField(max_length=80)
    visitor_contact = models.BigIntegerField()
    person_to_meet = models.CharField(max_length=80)
    visitor_addhar = models.BigIntegerField()