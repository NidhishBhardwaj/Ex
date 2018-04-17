# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from school_structure.models import School, SchoolClass, SchoolAssessmentExam, SchoolSubject
import datetime

# Create your models here.


def get_question_paper_folder(instance, filename):
    directory = str(datetime.datetime.now().year) + '/' + \
                instance.school.name + '/' + instance.assessment_exam.assessment_exam_name + '/' + instance.subject.subject + '/'
    return str(directory) + str(filename)


class ExaminationCalendar(models.Model):
    school = models.ForeignKey(School)
    assessment_exam = models.ForeignKey(SchoolAssessmentExam)
    date_from = models.DateField()
    date_to = models.DateField()


class QuestionPaper(models.Model):
    school = models.ForeignKey(School)
    assessment_exam = models.ForeignKey(SchoolAssessmentExam)
    subject = models.ForeignKey(SchoolSubject)
    question_paper = models.FileField(upload_to=get_question_paper_folder)


class DateSheet(models.Model):
    school = models.ForeignKey(School)
    assessment_exam = models.ForeignKey(SchoolAssessmentExam)
    date = models.DateField()
    standard = models.ForeignKey(SchoolClass)
    subject = models.ForeignKey(SchoolSubject)


