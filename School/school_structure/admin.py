# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from school_structure.models import Boards, Affiliation, State, District, City,\
    Address, Group, School, SchoolStream, SchoolSubject, SchoolClass, SchoolAssessmentExam, SchoolAssessmentStructure

# Register your models here.

admin.site.register([Boards, Affiliation, State, District, City,\
    Address, Group, School, SchoolStream, SchoolSubject, SchoolClass, SchoolAssessmentExam, SchoolAssessmentStructure])
