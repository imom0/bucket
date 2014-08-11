#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

from .views import CollectionListView

urlpatterns = patterns(
    'collection.views',
    url(r'^$', CollectionListView.as_view(), name='collection_index'),
)
