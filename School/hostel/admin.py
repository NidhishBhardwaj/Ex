# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from hostel.models import Hostel, HostelRoom, RoomStudentCrossref, HostelAttendance, HostelAssetType,\
    HostelMessAssetType, HostelAssetStore, HostelAssetStudentCrossref, HostelAssetComp, HostelAssetRoomCrossref,\
    HostelMessAssetStore, HostelAssetRequirement, HostelMessAssetRequirement

# Register your models here.


admin.site.register([Hostel, HostelRoom, RoomStudentCrossref, HostelAttendance, HostelAssetType,\
    HostelMessAssetType, HostelAssetStore, HostelAssetStudentCrossref, HostelAssetComp, HostelAssetRoomCrossref,\
    HostelMessAssetStore, HostelAssetRequirement, HostelMessAssetRequirement])