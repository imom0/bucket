#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.forms import ModelForm
from django.forms.models import modelformset_factory


from .models import Request


class RequestForm(ModelForm):

    class Meta:
        model = Request
        fields = ('protocol', 'host', 'path',
                  'method', 'headers', 'query_params', 'body')

RequestFormSet = modelformset_factory(Request, form=RequestForm)
