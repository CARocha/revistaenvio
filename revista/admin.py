from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class ArticulosInline(admin.StackedInline):
	model = Articulos
	extra = 1

class RevistasAdmin(ImportExportModelAdmin):
	inlines = [ArticulosInline]

class ArticulosAdmin(ImportExportModelAdmin):
	pass

class IdiomasAdmin(ImportExportModelAdmin):
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