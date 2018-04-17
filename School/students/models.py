# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from school_structure.models import School, SchoolClass, State, City, District, SchoolSubject, SchoolAssessmentExam
from scholarships.models import Scholarship

# Create your models here.


ATTENDANCE_CHOICES = (
    ('PR', 'Present'),
    ('PP', 'Partially Present'),
    ('HD', 'Half Day'),
    ('LV', 'Leave'),
    ('AB', 'Absent'),
    ('HO', 'Holiday'),
    ('WO', 'Weekly Off')
)


RESULT_CHOICES = (
    ('PSS', 'Pass'),
    ('EXC', 'Excellent'),
    ('CMP', 'Compartment'),
    ('FAL', 'Fail'),
    ('GRC', 'Grace')
)


class Student(models.Model):
    school = models.ForeignKey(School)
    student_code = models.CharField(max_length=80)
    student_first_name = models.CharField(max_length=50)
    student_middle_name = models.CharField(max_length=30)
    student_last_name = models.CharField(max_length=50)
    admission_number = models.IntegerField()
    registration_number = models.CharField(max_length=80)
    standard = models.ForeignKey(SchoolClass)
    roll_number = models.IntegerField()
    father_name = models.CharField(max_length=50)
    father_contact1 = models.BigIntegerField()
    father_contact2 = models.BigIntegerField()
    father_occupation = models.CharField(max_length=60)
    father_email = models.EmailField()
    mother_name = models.CharField(max_length=50)
    mother_contact1 = models.BigIntegerField()
    mother_contact2 = models.BigIntegerField()
    mother_occupation = models.CharField(max_length=60)
    mother_email = models.EmailField()
    address_line1 = models.CharField(max_length=80)
    address_line2 = models.CharField(max_length=80, null=True, blank=True)
    state = models.ForeignKey(State)
    district = models.ForeignKey(District)
    city = models.ForeignKey(City)
    pincode = models.IntegerField()
    is_hostler = models.BooleanField()
    scholarship_payment_done = models.BooleanField()
    scholarship_availed = models.ForeignKey(Scholarship, null=True, blank=True)
    mode_of_transport = models.CharField(max_length=10)
    fee_concession = models.IntegerField()
    fee_addition = models.IntegerField()


class StudentHistory(models.Model):
    student = models.ForeignKey(Student)
    historic_schools = models.ManyToManyField(School)


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student)
    school = models.ForeignKey(School)
    status = models.CharField(max_length=4,choices=ATTENDANCE_CHOICES)
    date = models.DateField()


class StudentAssesment(models.Model):
    school = models.ForeignKey(School)
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(SchoolSubject)
    theory_marks = models.IntegerField()
    pract_marks = models.IntegerField()
    total_marks = models.IntegerField()
    result = models.CharField(max_length=10, choices=RESULT_CHOICES)
    assesment_exam = models.ForeignKey(SchoolAssessmentExam)
    standard = models.ForeignKey(SchoolClass)


