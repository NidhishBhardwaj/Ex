# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from school_structure.models import School, SchoolClass
from students.models import Student


# Create your models here.


class FeeStructure(models.Model):
    school = models.ForeignKey(School)
    structure_name = models.CharField(max_length=50)
    classes = models.ManyToManyField(SchoolClass)
    monthly_tution_fee = models.IntegerField()
    monthly_extra_charges = models.IntegerField()



class FeeDefaulter(models.Model):
    school = models.ForeignKey(School)
    quarter = models.CharField(max_length=30)
    student = models.ForeignKey(Student)


class FeePaid(models.Model):
    school = models.ForeignKey(School)
    student = models.ForeignKey(Student)
    paid_amount = models.IntegerField()
    dues = models.IntegerField()
    quarter = models.CharField(max_length=30)
