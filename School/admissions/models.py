# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from school_structure.models import School
from students.models import Student

# Create your models here.


INQ_STATUS_CHOICES = (
    ('FR', 'Fresh'),
    ('SD', 'Selected'),
    ('NS', 'Not Selected'),
    ('IN', 'Initiated'),
    ('EX', 'Executed')
)


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('OTH', 'Others')
)


TRAVEL_CHOICES = (
    ('SF', 'Self'),
    ('BS', 'Bus')
)



class NewInquiry(models.Model):
    school = models.ForeignKey(School)
    inquiry_number = models.CharField(max_length=60)
    inq_from = models.ForeignKey(User)
    contact_number = models.BigIntegerField()
    contact_email = models.EmailField()
    status = models.CharField(max_length=10, choices=INQ_STATUS_CHOICES)
    child_name = models.CharField(max_length=150)
    for_class = models.IntegerField()
    child_dob = models.DateField()
    previous_class_grade = models.FloatField()
    for_stream = models.CharField(max_length=50,null=True, blank=True)


class NewAdmissionRequest(models.Model):
    school = models.ForeignKey(School)
    request_number = models.CharField(max_length=60)
    child_name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    sex = models.CharField(max_length=3, choices=GENDER_CHOICES)
    father_name = models.CharField(max_length=100)
    father_mobile = models.BigIntegerField()
    father_email = models.EmailField()
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_mobile = models.BigIntegerField()
    mother_email = models.EmailField()
    mother_occupation = models.CharField(max_length=100)
    prev_class_percent = models.FloatField()
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    model_of_transport = models.CharField(max_length=5, choices=TRAVEL_CHOICES)


class NewAdmission(models.Model):
    school = models.ForeignKey(School)
    student = models.ForeignKey(Student)
    session = models.CharField(max_length=30)


class LeftStudent(models.Model):
    school = models.ForeignKey(School)
    student = models.ForeignKey(Student)
    session = models.CharField(max_length=30)