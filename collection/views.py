#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json


from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.generic import (ListView, DetailView,
                                  CreateView)

from request.forms import RequestFormSet
from .models import Collection
from .forms import CollectionForm


class CollectionListView(ListView):

    model = Collection
    template_name = 'collection_list.jade'


class CollectionDetailView(DetailView):

    model = Collection
    template_name = 'collection_detail.jade'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        requests = self.object.request_set.all()
        context['request_form_set'] = RequestFormSet(queryset=requests)
        return context


class CollectionCreateView(CreateView):

    model = Collection
    form_class = CollectionForm
    template_name = 'collection_create.jade'
    success_url = reverse_lazy('collection_index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        return super(CollectionCreateView, self).form_valid(form)


@require_POST
def update_collection(request):
    data = {
        'status': 'OK'
    }
    return HttpResponse(content=json.dumps(data), status=200)
