# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.flatpages.models import FlatPage

class Flatpage(FlatPage):
    published = models.BooleanField(default=True, blank=True)
    scripts = models.TextField(blank=True)
    styles = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    description = models.TextField(blank=True)

class Menu(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(u"URL",max_length=50)
    index = models.IntegerField(u"Order")
    registration_required = models.BooleanField()
    
    class Meta:
        ordering = ('index',)
        verbose_name = u"Menu"
        verbose_name_plural = u"Menus"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.id
