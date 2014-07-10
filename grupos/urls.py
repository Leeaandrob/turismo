#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('grupos.views',
	url(r'^novo/$', 'grupo_create', name='grupo_create'),
	url(r'^lista/$','grupo_lista', name='grupo_lista'),
)