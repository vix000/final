from django.urls import path
from registers.views import RegisterListView, EntryListView


app_name = 'registers'

urlpatterns = [
    path('register/', RegisterListView.as_view(), name='registers-view'),
    path('entry/', EntryListView.as_view(), name='entries-view'),
]
