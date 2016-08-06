#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
"""
WSGI config for mtrk project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mtrk.settings")

application = get_wsgi_application()
