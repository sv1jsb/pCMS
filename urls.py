from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.MEDIA_ROOT}),
    url(r'fpg/',include('fpg.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

)
