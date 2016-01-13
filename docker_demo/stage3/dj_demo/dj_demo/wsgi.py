"""
WSGI config for dj_demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_demo.settings")

from django.conf import settings
from hello.models import Counter

Counter.objects.get_or_create(name=settings.STAT_NAME, defaults={'count':0})

application = get_wsgi_application()
