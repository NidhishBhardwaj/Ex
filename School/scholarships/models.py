# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from school_structure.models import School, SchoolClass

# Create your models here.


class Scholarship(models.Model):
    school = models.ForeignKey(School)
    scholarship_name = models.CharField(max_length=50)
    classes_eligible = models.ManyToManyField(SchoolClass)
    scholarship_amount = models.IntegerField()
    scholarship_eligibility = models.CharField(max_length=150)


class ScholarshipGranted(models.Model):
    school = models.ForeignKey(School)
    scholarship = models.ForeignKey(Scholarship)
