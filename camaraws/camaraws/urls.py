# Create your views here.
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.conf import settings
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'camaraws.views.home', name='home'),
    # url(r'^camaraws/', include('camaraws.foo.urls')),

    # Index
    url(r'^$', redirect_to, {'url' : '/index/'}),
    url(r'^index/$', 'camaraws.views.index'),
    url(r'^origem/$', 'camaraws.views.origem'),
    url(r'^ogrupo/$', 'camaraws.views.ogrupo'),

    #Serivço que retorna conteúdo para plotar o mapa
    url(r'^analises/cmsp/json/$', 'analises.views.json_cmsp'),
    url(r'^analises/cmsp/$', 'analises.views.cmsp'),
    url(r'^analises/cdep/$', 'analises.views.cdep'),
    url(r'^analises/senf/$', 'analises.views.senf'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)