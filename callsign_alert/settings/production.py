"""
Settings for production environment only
"""

import os
import encrypted_secrets
import urllib.parse

import dj_database_url

DEBUG = False
SECRET_KEY = encrypted_secrets.get_secret('secret_key')


ALLOWED_HOSTS = [
    "callsign-alert.fly.dev",  # fly.io development domain
]

DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL'),  # ensure this is set
        conn_max_age=600,
        conn_health_checks=True,
    )
}
