"""
Settings for development environment only
"""
import pathlib

DEBUG = True
SECRET_KEY = 'django-insecure-3$8#3t1j^tjx5t2#h1g4i4j%4$w4o#%#-8k^f!2'


ALLOWED_HOSTS = ["*"]

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
