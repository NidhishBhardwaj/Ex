# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from fees_management.models import FeeStructure, FeeDefaulter, FeePaid
# Register your models here.

admin.site.register([FeeStructure, FeeDefaulter, FeePaid])
