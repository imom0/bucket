#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.forms import ModelForm


from .models import Request


class RequestForm(ModelForm):

    class Meta:
        model = Request
        fields = ('scheme', 'netloc', 'path',
                  'method', 'headers', 'query', 'body')
