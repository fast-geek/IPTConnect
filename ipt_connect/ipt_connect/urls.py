from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from ipt_connect.views import home

import importlib
tournament_overview = importlib.import_module(
    f'{settings.INSTALLED_TOURNAMENTS[0]}.views').tournament_overview


urlpatterns = [
    # Examples:
    # url(r'^$', 'ipt_connect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    #url(r'^$', home, name='home'), #TemplateView.as_view(template_name='index.html')),#'ipt_connect.views.home'),
    url(r'^$', tournament_overview),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('loginas.urls')),
]

urlpatterns.extend(
    url(f'^{tournament}/', include(f'{tournament}.urls', namespace=tournament))
    for tournament in settings.INSTALLED_TOURNAMENTS)
admin.site.site_header = 'IPT administration'
