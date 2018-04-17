# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from students.models import  Student, StudentHistory, StudentAttendance

# Register your models here.

admin.site.register([Student, StudentHistory, StudentAttendance])
