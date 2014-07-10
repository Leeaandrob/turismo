from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'turismo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^destinos/',include('destinos.urls', namespace='destinos')),
    url(r'^grupos/',include('grupos.urls', namespace='grupos')),
)
