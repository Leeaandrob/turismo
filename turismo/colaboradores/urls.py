#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('turismo.colaboradores.views',
    url(r'^novo/$', 'colaborador_create', name='colaborador_create'),
    url(r'^editar/(?P<colaborador_id>\d+)/$', 'colaborador_edit', name='colaborador_edit'),
    url(r'^lista/$','colaborador_lista', name='colaborador_lista'),
    
    url(r'^upload_picture/$', 'upload_picture', name='upload_picture'),
    url(r'^save_uploaded_picture/$', 'save_uploaded_picture', name='save_uploaded_picture'),
)