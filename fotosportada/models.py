# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField
from revista.utils import get_file_path

# Create your models here.

class FotosPortada(models.Model):
	titulo = models.CharField(max_length=250)

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Fotos portada'
		verbose_name_plural = 'Fotos de las Portadas'

class Fotos(models.Model):
	portada = models.ForeignKey(FotosPortada)
	imagen = ImageField(upload_to=get_file_path, null=True, blank=True)
	frase = models.TextField()
	autor = models.CharField(max_length=250)

	fileDir = 'slider/'

	def __unicode__(self):
		return self.portada.titulo

	class Meta:
		verbose_name = 'Foto'
		verbose_name_plural = 'Fotos'
