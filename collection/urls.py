#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

from .views import CollectionListView, CollectionDetailView

urlpatterns = patterns(
    'collection.views',
    url(r'^$', CollectionListView.as_view(),
        name='collection_index'),
    url(r'^(?P<pk>\d+)/$', CollectionDetailView.as_view(),
        name='collection_detail'),
)
