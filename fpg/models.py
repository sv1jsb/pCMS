# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.flatpages.models import FlatPage

class Flatpage(FlatPage):
    published = models.BooleanField("Published", default=True, blank=True)
    keywords = models.TextField(verbose_name=u"Keywords", blank=True)
    description = models.TextField(verbose_name=u"Description", blank=True)

class Menu(models.Model):
    title = models.CharField(verbose_name=u"Title",max_length=50)
    url = models.CharField(verbose_name=u"URL",max_length=50)
    index = models.IntegerField(verbose_name=u"Order")
    registration_required = models.BooleanField(verbose_name=u"Registration required")
    
    class Meta:
        ordering = ('index',)
        verbose_name = u"Menu"
        verbose_name_plural = u"Menus"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.id
