import os

ENV = os.environ.get('ENV', "development").lower()

from .common import *  # noqa

if ENV == 'production':
    from .production import *  # noqa

if ENV == 'development':
    from .development import *  # noqa
