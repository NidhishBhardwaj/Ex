# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from admissions.models import NewAdmissionRequest, NewInquiry, NewAdmission, LeftStudent

# Register your models here.

admin.site.register([NewAdmissionRequest, NewInquiry, NewAdmission, LeftStudent])