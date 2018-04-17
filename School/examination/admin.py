# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from examination.models import ExaminationCalendar, QuestionPaper, DateSheet

# Register your models here.


admin.site.register([ExaminationCalendar, QuestionPaper, DateSheet])