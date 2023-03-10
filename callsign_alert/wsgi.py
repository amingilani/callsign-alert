"""
WSGI config for callsign_alert project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import encrypted_secrets


encrypted_secrets.load_secrets()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "callsign_alert.settings")

application = get_wsgi_application()
