#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from django.forms import ModelForm

from .models import Collection


class CollectionForm(ModelForm):

    class Meta:
        model = Collection
        fields = ('name', 'description')
