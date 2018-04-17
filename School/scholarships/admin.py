# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from scholarships.models import Scholarship, ScholarshipGranted
# Register your models here.


admin.site.register([Scholarship, ScholarshipGranted])