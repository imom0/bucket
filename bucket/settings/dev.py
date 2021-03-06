#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']
SECRET_KEY = '+*qfu*s7%81p=r8)zi#^#ie47x1#a^#ycxl37#df-ul$*uq@(s'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.db'),
    }
}
