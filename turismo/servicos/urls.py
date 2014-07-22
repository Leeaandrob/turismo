#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('turismo.servicos.views',
    url(r'^novo/$', 'servico_create', name='servico_create'),
    url(r'^editar/(?P<servico_id>\d+)/$', 'servico_edit', name='servico_edit'),
    url(r'^lista/$','servico_lista', name='servico_lista'),
)