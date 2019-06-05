from .base import *

DEBUG = True
SECRET_KEY = 'raq^q9&#@0us0#@p^mtpnuc@)d*w_k@+913a(icq2ts2-#gt+2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'scraper_db',
        'USER': 'scraper_user',
        'PASSWORD': 'ug123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_RESET_VALUE = 60
BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_IMPORTS = ('core.tasks',)

FALCON_HOST = '0.0.0.0'
FALCON_PORT = 5000
FALCON_RESOURCE = 'main'
FALCON_RESULTS_RESOURCE = 'results'
FALCON_SCHEMA = 'http'
