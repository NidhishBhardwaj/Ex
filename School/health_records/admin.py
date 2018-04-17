# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from health_records.models import HealthCheckupCampaign, HealthRecords
# Register your models here.


admin.site.register([HealthCheckupCampaign, HealthRecords])