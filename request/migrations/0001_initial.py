# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_url', models.CharField(max_length=200, verbose_name='\u57fa\u5740')),
                ('method', models.CharField(max_length=10, verbose_name='HTTP\u65b9\u6cd5', choices=[(b'HEAD', b'HEAD'), (b'GET', b'GET'), (b'POST', b'POST')])),
                ('headers', models.TextField(verbose_name='HTTP\u5934', blank=True)),
                ('query_params', models.TextField(verbose_name='Query Params', blank=True)),
                ('body', models.TextField(verbose_name='Body', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('collection', models.ForeignKey(verbose_name='\u6d4b\u8bd5\u96c6', to='collection.Collection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
