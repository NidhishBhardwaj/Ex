# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from library.models import IssueRuleBook, Book

# Register your models here.


admin.site.register([IssueRuleBook, Book])