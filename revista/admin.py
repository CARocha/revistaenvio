# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.flatpages.models import FlatPage
# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from django import forms
from ckeditor.widgets import CKEditorWidget

class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage
        fields = '__all__'


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm

class ArticulosInline(admin.StackedInline):
    exclude = ('cambio','codigoml',)
    model = Articulos
    extra = 1

class RevistasAdmin(ImportExportModelAdmin):
    #inlines = [ArticulosInline]
    list_display = ['numero','ididioma','volumen','mes','articulos_conteo']
    list_display_links = ['numero','ididioma']
    search_fields = ['numero',]
    list_filter = ['ididioma', 'mes', 'ano',]

    def articulos_conteo(self, obj):
        return '%s'%(obj.articulos_set.count())
    articulos_conteo.short_description = '# articulos'

class ArticulosAdmin(ImportExportModelAdmin):
    exclude = ('cambio','codigoml',)
    list_display = ['id', 'titulo','revista','idioma', 'idzona']
    list_display_links = ['id','titulo','revista']
    list_filter = ['idzona','idioma']
    ordering = ('-id',)

class IdiomasAdmin(ImportExportModelAdmin):
    pass

class ZonasAdmin(ImportExportModelAdmin):
    pass

class TemasAdmin(ImportExportModelAdmin):
    pass

class AutoresAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nombre','email']
    search_fields = ['nombre']

class EnlacesAdmin(ImportExportModelAdmin):
    pass

class TipoAdmin(ImportExportModelAdmin):
    pass

class EnvioAdmin(ImportExportModelAdmin):
    list_display = ['id', 'institucion','tnombre', 'idtipo', 'idpais', 'nueva']
    list_display_links = ['id', 'institucion', 'tnombre']


class PaisAdmin(ImportExportModelAdmin):
    list_display = ['id', 'pais']

class colorAdmin(ImportExportModelAdmin):
    list_display = ['id','color1', 'color2']
# Register your models here.
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Revistas, RevistasAdmin)
admin.site.register(Idiomas, IdiomasAdmin)
admin.site.register(Zonas, ZonasAdmin)
admin.site.register(Temas, TemasAdmin)
admin.site.register(Autores, AutoresAdmin)
admin.site.register(Enlaces, EnlacesAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Envio, EnvioAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(ColoresRevista, colorAdmin)
#FlatPages
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
