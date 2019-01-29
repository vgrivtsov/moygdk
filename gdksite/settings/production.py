from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass



ALLOWED_HOSTS = ['95.213.236.166', 'moygdk.ru', 'www.moygdk.ru']
