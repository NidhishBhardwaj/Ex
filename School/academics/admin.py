# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from academics.models import AnnualSyllabus, AcademicProgress, HomeworkReport

# Register your models here.

admin.site.register([AnnualSyllabus, AcademicProgress, HomeworkReport])