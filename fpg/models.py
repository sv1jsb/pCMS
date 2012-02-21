# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.flatpages.models import FlatPage

class Flatpage(FlatPage):
    published = models.BooleanField("Δημοσιευμένη", default=True, blank=True)

class Menu(models.Model):
    title = models.CharField(verbose_name=u"Τίτλος",max_length=50)
    url = models.CharField(verbose_name=u"URL",max_length=50)
    index = models.IntegerField(verbose_name=u"Σειρά")
    registration_required = models.BooleanField(verbose_name=u"Απαιτείται εγγραφή")
    
    class Meta:
        ordering = ('index',)
        verbose_name = u"Μενού"
        verbose_name_plural = u"Μενού"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.id
