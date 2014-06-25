#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('destinos.views',
	url(r'^novo/$', 'destino_create', name='destino_create'),
	url(r'^lista/$','destino_lista', name='destino_lista'),
)