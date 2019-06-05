import json
import requests
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView
from django.conf import settings
from django.shortcuts import render

from registers.models import Registry
from .forms import ScraperForm
from .tasks import handle_scraper_queue


class MainView(TemplateView):
    template_name = 'core/main.html'


class ScraperView(CreateView):

    def post(self, request, *args, **kwargs):
        result = handle_scraper_queue.delay(request.POST.dict())
        if request.user.is_authenticated:
            Registry.objects.create(query_string=request.POST.get('identifier'), user=request.user)
        return HttpResponseRedirect(reverse_lazy('main-view'))


class ResultsView(TemplateView):
    template_name = 'core/results.html'

    def prepare_url(self, schema, host, port, resource):
        return f'{schema}://{host}:{port}/{resource}'

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        url = self.prepare_url(settings.FALCON_SCHEMA, settings.FALCON_HOST, settings.FALCON_PORT, settings.FALCON_RESULTS_RESOURCE)
        payload = {
            "filename": f'clothing-{self.request.user.email}'
        }
        r = requests.get(url, params=payload)
        items = json.loads(r.text)   
        result = []
        for elem in items:
            for k, v in elem.items():
                tmp = {}
                tmp['name'] = k
                tmp['image'] = v['image']
                tmp['url'] = v['url']
                tmp['price'] = v['price']
                result.append(tmp)
        args = {
            "items": result,
        }
        return render(request, self.template_name, args)


    def check_if_file_is_empty(self, file_content_length):
        return True if file_content_length == 0 else False
            
 
