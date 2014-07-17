#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('turismo.destinos.views',
	url(r'^novo/$', 'destino_create', name='destino_create'),
	url(r'^editar/(?P<destino_id>\d+)/$', 'destino_edit', name='destino_edit'),
	url(r'^lista/$','destino_lista', name='destino_lista'),
)