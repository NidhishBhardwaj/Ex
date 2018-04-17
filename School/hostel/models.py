# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from school_structure.models import School
from django.contrib.auth.models import User
from students.models import Student

# Create your models here.


ATTENDANCE_CHOICES = (
    ('PR', 'Present'),
    ('PP', 'Partially Present'),
    ('HD', 'Half Day'),
    ('LV', 'Leave'),
    ('AB', 'Absent'),
    ('HO', 'Holiday'),
    ('WO', 'Weekly Off')
)


class Hostel(models.Model):
    school = models.ForeignKey(School)
    hostel_head_incharge = models.ForeignKey(User)


class HostelRoom(models.Model):
    hostel = models.ForeignKey(Hostel)
    room_floor = models.IntegerField()
    hostel_block = models.CharField(max_length=10)
    room_warden = models.ForeignKey(User)
    bed_available = models.BooleanField()
    number_of_beds = models.IntegerField()
    room_number = models.CharField(max_length=20)


class RoomStudentCrossref(models.Model):
    room = models.ForeignKey(HostelRoom)
    student = models.ManyToManyField(Student)
    hostel = models.ForeignKey(Hostel)


class HostelAttendance(models.Model):
    hostel = models.ForeignKey(Hostel)
    student = models.ForeignKey(Student)
    attendance = models.CharField(max_length=5, choices=ATTENDANCE_CHOICES)
    date = models.DateField()
    attendance_marked_by = models.ForeignKey(User)


class HostelAssetType(models.Model):
    hostel = models.ForeignKey(Hostel)
    asset_type = models.CharField(max_length=30)
    is_consumable = models.BooleanField()
    is_replacable = models.BooleanField()
    replacement_duration = models.IntegerField()
    inspection_period = models.IntegerField()


class HostelMessAssetType(models.Model):
    hostel = models.ForeignKey(Hostel)
    asset_type = models.CharField(max_length=30)
    is_consumable = models.BooleanField()
    is_replacable = models.BooleanField()
    replacement_duration = models.IntegerField()
    inspection_period = models.IntegerField()


class HostelAssetStore(models.Model):
    hostel = models.ForeignKey(Hostel)
    asset_name = models.CharField(max_length=40)
    asset_type = models.ForeignKey(HostelAssetType)
    quantity = models.IntegerField()
    inspection_date = models.DateField()
    inspection_count = models.IntegerField()
    added_on = models.DateField(auto_now=True)
    defective_count = models.IntegerField()


class HostelAssetStudentCrossref(models.Model):
    hostel = models.ForeignKey(Hostel)
    asset = models.ForeignKey(HostelAssetStore)
    student = models.ForeignKey(Student)
    status = models.CharField(max_length=5)


class HostelAssetComp(models.Model):
    hostel = models.ForeignKey(Hostel)
    asset_student = models.ForeignKey(HostelAssetStudentCrossref)


class HostelAssetRoomCrossref(models.Model):
    hostel = models.ForeignKey(Hostel)
    room = models.ForeignKey(HostelRoom)
    asset = models.ForeignKey(HostelAssetStore)


class HostelMessAssetStore(models.Model):
    hostel = models.ForeignKey(Hostel)
    asset_name = models.CharField(max_length=40)
    asset_type = models.ForeignKey(HostelAssetType)
    quantity = models.IntegerField()
    inspection_date = models.DateField()
    inspection_count = models.IntegerField()
    added_on = models.DateField(auto_now=True)
    defective_count = models.IntegerField()


class HostelAssetRequirement(models.Model):
    hostel = models.ForeignKey(Hostel)
    asset_type = models.ForeignKey(HostelAssetType)
    asset_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10)
    approved_count = models.IntegerField()


class HostelMessAssetRequirement(models.Model):
    hostel = models.ForeignKey(Hostel)
    asset_type = models.ForeignKey(HostelAssetType)
    asset_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10)
    approved_count = models.IntegerField()