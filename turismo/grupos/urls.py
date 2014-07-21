#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('turismo.grupos.views',
	url(r'^novo/$', 'grupo_create', name='grupo_create'),
    url(r'^editar/(?P<grupo_id>\d+)/$','grupo_edit', name='grupo_edit'),
	url(r'^lista/$','grupo_lista', name='grupo_lista'),
    url(r'^inserir_ao_grupo/(?P<grupo_id>\d+)/(?P<cliente_id>\d+)/$','inserir_ao_grupo', name='inserir_ao_grupo')
)