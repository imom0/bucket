#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.views.generic import ListView, DetailView

from .models import Collection


class CollectionListView(ListView):

    model = Collection
    template_name = 'collection_list.jade'


class CollectionDetailView(DetailView):

    model = Collection
    template_name = 'collection_detail.jade'
