#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.db import models

from .constants import METHODS


class Request(models.Model):
    collection = models.ForeignKey('collection.Collection',
                                   verbose_name=u'测试集')
    protocol = models.CharField(u'协议', max_length=10)
    host = models.CharField(u'host', max_length=200)
    path = models.CharField(u'endpoint', max_length=8192)
    method = models.CharField(u'HTTP方法', max_length=10, choices=METHODS)
    headers = models.TextField(u'HTTP头', blank=True)
    query_params = models.TextField(u'Query Params', blank=True)
    body = models.TextField(u'Body', blank=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)
