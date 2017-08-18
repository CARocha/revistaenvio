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
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.html import format_html

class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget())
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
    fields = ('volumen','ano','mes','numero','ididioma','color','portada')
    list_display = ['numero','ididioma','volumen','mes','articulos_conteo']
    list_display_links = ['numero','ididioma']
    search_fields = ['numero',]
    list_filter = ['ididioma', 'mes', 'ano',]

    def articulos_conteo(self, obj):
        return '%s'%(obj.articulos_set.count())
    articulos_conteo.short_description = '# articulos'

    class Media:
        js = ('/static/js/colorAdmin.js',)

class ArticulosAdmin(ImportExportModelAdmin):
    exclude = ('cambio','codigoml',)
    list_display = ['id', 'titulo','revista','idioma', 'idzona']
    list_display_links = ['id','titulo','revista']
    search_fields = ['titulo','texto']
    list_filter = ['idzona','idioma','revista__mes', 'revista__ano']
    ordering = ('-id',)

class IdiomasAdmin(ImportExportModelAdmin):
    pass

class ZonasAdmin(ImportExportModelAdmin):
    list_display = ('zona_es', 'zona_en')
    search_fields = ('zona_es', 'zona_en')

class TemasAdmin(ImportExportModelAdmin):
    list_display = ('tema_es', 'tema_en')
    search_fields = ('tema_es', 'tema_en')

class AutoresAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nombre','email','nombre_en']
    search_fields = ['nombre', 'nombre_en']

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
    list_display = ['id','color1', 'color2', 'color', 'colored_name']

    def colored_name(self, obj):
        return format_html('<span style="background-color:{};width:40px; heigth:20px; color:{};">COLOR</span>',obj.color1,obj.color1)
    colored_name.short_description = 'Color visual'


# Register your models here.
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Revistas, RevistasAdmin)
admin.site.register(Idiomas, IdiomasAdmin)
admin.site.register(Zonas, ZonasAdmin)
admin.site.register(Temas, TemasAdmin)
admin.site.register(Autores, AutoresAdmin)
#admin.site.register(Enlaces, EnlacesAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Envio, EnvioAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(ColoresRevista, colorAdmin)
#FlatPages
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
