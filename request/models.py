#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.db import models

from .constants import METHODS


class Request(models.Model):
    collection = models.ForeignKey('collection.Collection',
                                   verbose_name=u'测试集')
    is_ssl = models.BooleanField(u'是否使用HTTPS', default=False)
    host = models.CharField(u'HOST', max_length=200)
    method = models.CharField(u'HTTP方法', max_length=10, choices=METHODS)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
