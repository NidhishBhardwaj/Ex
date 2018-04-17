# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from school_structure.models import School, SchoolClass
from students.models import Student
import datetime
# Create your models here.


def get_file_path(instance,filename):
    directory = str(datetime.datetime.now().year) + '/' + \
                instance.school.name + '/' + instance.student.student_first_name + '/'
    return str(directory) + str(filename)


class HealthCheckupCampaign(models.Model):
    school = models.ForeignKey(School)
    date_from = models.DateField()
    date_to = models.DateField()
    classes = models.ManyToManyField(SchoolClass)
    added_on = models.DateField(auto_now=True)


class HealthRecords(models.Model):
    school = models.ForeignKey(School)
    student = models.ForeignKey(Student)
    file = models.FileField(upload_to=get_file_path)