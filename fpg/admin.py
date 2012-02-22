# -*- coding: utf-8 -*-
from django.contrib import admin
from fpg.models import Flatpage, Menu
from django.contrib.flatpages.admin import FlatpageForm,FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

class FpgForm(FlatpageForm):

    class Meta:
        model = Flatpage


class FpgAdmin(FlatPageAdmin):
    form = FpgForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'published','sites')}),
        ('Other choices', {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
        ('Meta tags', {'classes': ('collapse',), 'fields': ('keywords', 'description')}),
    )
    list_display = ('url', 'title','published','registration_required')
    list_filter = ('published','sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')

    class Media:
        js = ('admin/tiny_mce.js','admin/textareas.js')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('index','title','url','registration_required')
    list_filter = ('registration_required',)
    search_fields = ('url', 'title')
    
admin.site.unregister(FlatPage)
admin.site.register(Flatpage,FpgAdmin)
admin.site.register(Menu, MenuAdmin)
