from django.conf.urls.defaults import *

urlpatterns = patterns('fpg.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
