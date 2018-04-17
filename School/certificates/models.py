# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from school_structure.models import School
from students.models import Student

# Create your models here.


CERTIFICATE_TYPE_CHOICES=(
    ('TC', 'Transfer Certificate'),
    ('CC', 'Character Certificate'),
    ('BC', 'Bonafeid Certificate'),
    ('LC', 'Leaving Certificate'),
    ('MC', 'Migration Certificate')
)


class IssuedCertificate(models.Model):
    school = models.ForeignKey(School)
    issued_to = models.ForeignKey(Student)
    issue_date = models.DateField()
    issue_reason = models.CharField(max_length=100)
    certificate_type = models.CharField(max_length=7, choices=CERTIFICATE_TYPE_CHOICES)
    issued_by = models.ForeignKey(User)


class SavedTemplate(models.Model):
    school = models.ForeignKey(School)
    certificate_type = models.CharField(max_length=7, choices=CERTIFICATE_TYPE_CHOICES)
    header_text = models.TextField()
    body_text = models.TextField()
    footer_text = models.TextField()
