import requests
from config.celery import app
from django.conf import settings


def prepare_url(schema, host, port, resource):
    return f'{schema}://{host}:{port}/{resource}'
    

@app.task
def handle_scraper_queue(payload):
    url = prepare_url(settings.FALCON_SCHEMA, settings.FALCON_HOST, settings.FALCON_PORT, settings.FALCON_RESOURCE)
    try:
        r = requests.get(url=url, params=payload)
    except Exception as e:
        pass
