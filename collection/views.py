#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.core.urlresolvers import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView)

from .models import Collection
from .forms import CollectionForm


class CollectionListView(ListView):

    model = Collection
    template_name = 'collection_list.jade'


class CollectionDetailView(DetailView):

    model = Collection
    template_name = 'collection_detail.jade'


class CollectionCreateView(CreateView):

    model = Collection
    form_class = CollectionForm
    template_name = 'collection_create.jade'
    success_url = reverse_lazy('collection_index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        return super(CollectionCreateView, self).form_valid(form)
