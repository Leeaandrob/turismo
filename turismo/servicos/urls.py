#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('turismo.servicos.views',
    url(r'^novo/$', 'servicos_create', name='servicos_create'),
    url(r'^editar/(?P<servicos_id>\d+)/$', 'servicos_edit', name='servicos_edit'),
    url(r'^lista/$','servicos_lista', name='servicos_lista'),
)