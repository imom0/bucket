#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json


from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import (ListView, DetailView,
                                  CreateView)

from request.forms import RequestForm
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


@require_http_methods(['GET', 'POST'])
def collection_requests(request, pk):
    try:
        collection = Collection.objects.get(pk=pk)
        requests = collection.request_set.all()
    except Collection.DoesNotExist:
        requests = []
    data = {
        'meta': {
            'status': 'OK'
        },
        'data': [req.as_dict() for req in requests]
    }
    return HttpResponse(content=json.dumps(data), status=200)
