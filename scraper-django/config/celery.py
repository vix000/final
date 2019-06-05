import os
from celery import Celery
from celery.schedules import crontab


HANDLE_CONFIGURATION_TASK_PERIOD_IN_SECONDS = 100
UPDATE_CONFIGURATION_TASK_PERIOD_IN_SECONDS = 5
ABANDONED_DOMAINS_TASK_PERIOD_IN_DAYS = 1
DOMAIN_EXPIRATION_TIME_IN_DAYS = 5

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

app = Celery('core')
app.config_from_object('django.conf:settings')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
