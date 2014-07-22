from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'turismo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^destinos/',include('turismo.destinos.urls', namespace='destinos')),
    url(r'^grupos/',include('turismo.grupos.urls', namespace='grupos')),
    url(r'^clientes/',include('turismo.clientes.urls',namespace='clientes')),
    url(r'^colaboradores/',include('turismo.colaboradores.urls',namespace='colaboradores')),
    url(r'^servicos/',include('turismo.servicos.urls',namespace='servicos')),
)
