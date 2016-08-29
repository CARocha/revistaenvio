from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class ArticulosAdmin(ImportExportModelAdmin):
	list_display = ('id', 'titulo')

class IdiomasAdmin(ImportExportModelAdmin):
	pass

class RevistasAdmin(ImportExportModelAdmin):
	pass

class ZonasAdmin(ImportExportModelAdmin):
	pass

class TemasAdmin(ImportExportModelAdmin):
	pass

class AutoresAdmin(ImportExportModelAdmin):
	pass

class EnlacesAdmin(ImportExportModelAdmin):
	pass

class TipoAdmin(ImportExportModelAdmin):
	pass

class EnvioAdmin(ImportExportModelAdmin):
	pass

class PaisAdmin(ImportExportModelAdmin):
	pass

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