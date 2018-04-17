# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE_CHOICES = (
    ('PR', 'Private'),
    ('CG', 'Central Government'),
    ('SG', 'State Government'),
    ('SCG', 'Semi Central Government'),
    ('SSG', 'Semi State Government'),
)


EDUCATION_TYPE_CHOICES = (
    ('G', 'GIRLS'),
    ('B', 'BOYS'),
    ('CoEd', 'CO-ED')
)


EDUCATION_LEVEL_CHOICES = (
    ('PS', 'Play School'),
    ('PR', 'Primary'),
    ('SC', 'Secondary'),
    ('SR', 'Senior Secondary')
)


# model for keeping track of various boards
class Boards(models.Model):
    board = models.CharField(max_length=200)
    board_abbreviation = models.CharField(max_length=20)

    def __str__(self):
        return self.board_abbreviation


# model for maintaining various affiliation data
class Affiliation(models.Model):
    board = models.ForeignKey(Boards, on_delete=models.CASCADE)
    affiliation_number = models.BigIntegerField()
    affiliation_year = models.DateField()

    def __str__(self):
        return self.affiliation_number


# model for keeping list of states of country
class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# model for keeping list of districts in a state
class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# model for keeping list of cities in a district
class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# model for storing various addresses in a city
class Address(models.Model):
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=80, blank=True, null=True)
    address_line3 = models.CharField(max_length=70, blank=True, null=True)
    state = models.ForeignKey(State)
    district = models.ForeignKey(District)
    city = models.ForeignKey(City)
    pincode = models.IntegerField()

    def __str__(self):
        return self.address_line1 + " \n" + self.address_line2 + " \n" + self.address_line3


# Group model is the table for the information of the Main group
# running multiple schools in different cities
class Group(models.Model):
    name = models.CharField(max_length=100)
    boards = models.ManyToManyField(Boards, blank=True)
    head_office = models.CharField(max_length=100)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    address = models.ForeignKey(Address)

    def __str__(self):
        return self.name


# model for maintaining list of registered schools
class School(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    education_type = models.CharField(max_length=5, choices=EDUCATION_TYPE_CHOICES)
    education_level = models.CharField(max_length=5, choices=EDUCATION_LEVEL_CHOICES)
    affiliation = models.ForeignKey(Affiliation)
    address = models.ForeignKey(Address)
    group = models.ForeignKey(Group)

    def __str__(self):
        return self.name


# model for maintaining list of streams available in a school
class SchoolStream(models.Model):
    School = models.ForeignKey(School)
    stream_name = models.CharField(max_length=50)

    def __str__(self):
        return self.stream_name


# model for maintaining list of subjects taught in school
class SchoolSubject(models.Model):
    school = models.ForeignKey(School)
    subject = models.CharField(max_length=30)
    subject_hod = models.ForeignKey(User)

    def __str__(self):
        return self.subject


# model for maintaining list of classes in a school
class SchoolClass(models.Model):
    school = models.ForeignKey(School)
    standard = models.IntegerField()
    section = models.CharField(max_length=15)
    stream = models.ForeignKey(SchoolStream, null=True, blank=True)
    subjects = models.ManyToManyField(SchoolSubject)
    class_teacher = models.ForeignKey(User)

    def __str__(self):
        return str(self.standard) + "-" + self.section


class SchoolAssessmentExam(models.Model):
    school = models.ForeignKey(School)
    assessment_exam_name = models.CharField(max_length=30)
    classes = models.ManyToManyField(SchoolClass)


class SchoolAssessmentStructure(models.Model):
    school = models.ForeignKey(School)
    assesment_exam = models.ForeignKey(SchoolAssessmentExam)
    max_marks_theory = models.IntegerField()
    max_marks_practical = models.IntegerField()
    annual_weightage = models.FloatField()




