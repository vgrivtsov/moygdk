from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gdksite',
        'PASSWORD': 'vic83890',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['95.213.236.166', 'moygdk.ru', 'www.moygdk.ru']
