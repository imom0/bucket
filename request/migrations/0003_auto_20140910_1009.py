# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20140818_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='query_params',
            new_name='query',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='protocol',
            new_name='scheme',
        ),
        migrations.RemoveField(
            model_name='request',
            name='host',
        ),
        migrations.AddField(
            model_name='request',
            name='netloc',
            field=models.CharField(default='example.com:8080', max_length=200, verbose_name='netloc'),
            preserve_default=False,
        ),
    ]
