from django.shortcuts import render
from django.views.generic import ListView
from .models import Registry, Entry

# Create your views here.


class RegisterListView(ListView):
    template_name = "registers/list.html"
    context_object_name = 'registers'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Registry.objects.filter(user=self.request.user)


class EntryListView(ListView):
    template_name = "entries/list.html"
    context_object_name = 'entries'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Entry.objects.all()
