from django.contrib import admin
from .models import FotosPortada, Fotos

class FotosInline(admin.TabularInline):
	model = Fotos
	extra = 1

class FotosPortadaAdmin(admin.ModelAdmin):
	inlines = [FotosInline]

# Register your models here.
