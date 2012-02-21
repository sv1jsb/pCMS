from django.conf.urls.defaults import *
from fpg.extra_views import search, elfinder_mce, elfinder_connector_mce
urlpatterns = patterns('',
    url(r'^search/$',search,{},name='search'),
    url(r'^elfinder_mce/$',elfinder_mce,{},name='elfinder_mce'),
    url(r'^elfinder_connector_mce/$',elfinder_connector_mce,{},name='elfinder_connector_mce'),
)
