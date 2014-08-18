# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='host',
            field=models.CharField(default='example.com', max_length=200, verbose_name='host'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='path',
            field=models.CharField(default='/', max_length=8192, verbose_name='endpoint'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='protocol',
            field=models.CharField(default='http', max_length=10, verbose_name='\u534f\u8bae'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='request',
            name='base_url',
        ),
    ]
