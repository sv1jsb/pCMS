# -*- coding: utf-8 -*- 

from django.conf import settings
from django.contrib.sites.models import Site

def fpg_context(request):
    site = Site.objects.get_current()
    return {
        "SITE_NAME": site.name,
        "SITE_DOMAIN": site.domain
    }
