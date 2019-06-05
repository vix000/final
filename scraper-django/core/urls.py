"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import MainView, ScraperView, ResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="main-view"),
    path('scraper', ScraperView.as_view(), name="scraper-view"),
    path('results', ResultsView.as_view(), name="results-view"),
    path('users/', include('users.urls', namespace='users')),
    path('registers/', include('registers.urls', namespace='registers')),
    path('registration/', include('django.contrib.auth.urls')),
]
