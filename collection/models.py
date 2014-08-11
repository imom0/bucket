#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.db import models


class Collection(models.Model):
    name = models.CharField(u'名称', max_length=100)
    created_by = models.ForeignKey('auth.User', verbose_name=u'创建者')
    description = models.TextField(u'描述', blank=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True)

    unique_together = ('created_by_id', 'name')
