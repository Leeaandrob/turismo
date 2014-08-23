#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('turismo.grupos.views',
	url(r'^novo/$', 'grupo_create', name='grupo_create'),
    url(r'^editar/(?P<grupo_id>\d+)/$','grupo_edit', name='grupo_edit'),
	url(r'^lista/$','grupo_lista', name='grupo_lista'),
    url(r'^inserir_ao_grupo/(?P<grupo_id>\d+)/(?P<cliente_id>\d+)/$','inserir_ao_grupo', name='inserir_ao_grupo'),
    url(r'^remover_do_grupo/(?P<grupo_id>\d+)/(?P<cliente_id>\d+)/$','remover_do_grupo', name='remover_do_grupo'),
    
    url(r'^clientes/(?P<grupo_id>\d+)/$','clientes_grupo', name='clientes_grupo'),
    url(r'^add_grupo/$','add_grupo', name='add_grupo'),
    url(r'^rm_grupo/$','rm_grupo', name='rm_grupo'),

    url(r'^colaboradores/(?P<grupo_id>\d+)/$','colaboradores_grupo', name='colaboradores_grupo'),
    url(r'^add_colaborador_grupo/$','add_colaborador_grupo', name='add_colaborador_grupo'),
    url(r'^rm_colaborador_grupo/$','rm_colaborador_grupo', name='rm_colaborador_grupo'),

    url(r'^roteiros/(?P<grupo_id>\d+)/$','roteiro_create', name='roteiro_create'),
    url(r'^roteiros/lista/(?P<grupo_id>\d+)/$','roteiro_lista', name='roteiro_lista'),
    url(r'^roteiros/(?P<roteiro_id>\d+)$','roteiro_edit', name='roteiro_edit'),
    
    url(r'^relatorios/(?P<grupo_id>\d+)/$','relatorio_grupo', name='relatorio_grupo'),
    url(r'^relatorios/1/(?P<grupo_id>\d+)/$','relatorio_clientes_telefone', name='relatorio_clientes_telefone'),
    url(r'^relatorios/2/(?P<grupo_id>\d+)/$','relatorio_clientes_rg', name='relatorio_clientes_rg'),
)