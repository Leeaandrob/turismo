#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('turismo.clientes.views',
    url(r'^novo/$', 'cliente_create', name='cliente_create'),
    url(r'^editar/(?P<cliente_id>\d+)/$', 'cliente_edit', name='cliente_edit'),
    url(r'^lista/$','cliente_lista', name='cliente_lista'),
)