from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



class ArticulosInline(admin.StackedInline):
    model = Articulos
    extra = 1

class RevistasAdmin(ImportExportModelAdmin):
    inlines = [ArticulosInline]
    list_display = ['id','volumen','ano','mes','numero','ididioma']
    list_display_links = ['id','volumen','numero']

class ArticulosAdmin(ImportExportModelAdmin):
    pass

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
