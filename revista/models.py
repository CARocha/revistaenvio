# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
from .utils import get_file_path

class Idiomas(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    idioma = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.idioma

    class Meta:
        db_table = 'idiomas'
        verbose_name='Idioma'
        verbose_name_plural='Idiomas'

class Zonas(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    zona = models.CharField(max_length=50, blank=True, null=True)
    relevancia = models.IntegerField(blank=True, null=True)
    zona_en = models.CharField(max_length=50, blank=True, null=True)
    zona_es = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.zona

    class Meta:
        db_table = 'zonas'
        verbose_name='Zona'
        verbose_name_plural='Zonas'
        ordering = ('zona',)

class Temas(models.Model):
    tema = models.CharField(max_length=150, blank=True, null=True)
    tema_en = models.CharField(max_length=150, blank=True, null=True)
    tema_es = models.CharField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.tema

    class Meta:
        db_table = 'temas'
        verbose_name='Tema'
        verbose_name_plural='Temas'
        ordering = ('tema',)

class Autores(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=150, blank=True, null=True)
    email = models.CharField(_('Correo'), max_length=50, blank=True, null=True)
    titulo = models.CharField(_('Titulo'), max_length=50, blank=True, null=True)
    cargo = models.TextField(_('Cargo'), blank=True, null=True)
    nota = models.TextField(_('Nota'), blank=True, null=True)
    nombre_en = models.CharField(_('Nombre ingles'), max_length=150, blank=True, null=True)
    nombre_es = models.CharField(_('Nombre en español'), max_length=150, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'autores'
        verbose_name= _('Autor')
        verbose_name_plural= _('Autores')
        ordering = ('nombre',)

CHOICES_MES = (
        (1, _('Enero')),
        (2, _('Febrero')),
        (3, _('Marzo')),
        (4, _('Abril')),
        (5, _('Mayo')),
        (6, _('Junio')),
        (7, _('Julio')),
        (8, _('Agosto')),
        (9, _('Septiembre')),
        (10, _('Octubre')),
        (11, _('Noviembre')),
        (12, _('Diciembre'))
    )

class ColoresRevista(models.Model):
    color1 = models.CharField(max_length=50, null=True, blank=True)
    color2 = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.color1

class Revistas(models.Model):
    volumen = models.IntegerField()
    ano = models.IntegerField('Año', blank=True, null=True)
    mes = models.IntegerField(choices=CHOICES_MES, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    ididioma = models.ForeignKey(Idiomas, verbose_name='idioma')
    nota = models.TextField(blank=True, null=True)
    color = models.ForeignKey(ColoresRevista, blank=True, null=True)
    portada = ImageField(upload_to=get_file_path, null=True, blank=True)

    fileDir = 'portadas/'

    def __unicode__(self):
        return u'%s %s: Número: %s - Idioma: %s' % (str(self.get_mes_display()),str(self.ano),str(self.numero),self.ididioma)

    class Meta:
        db_table = 'revistas'
        verbose_name='Revista'
        verbose_name_plural='Revistas'
        ordering = ('-numero',)

class Articulos(models.Model):
    revista = models.ForeignKey(Revistas)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    idioma = models.ForeignKey(Idiomas, null=True, blank=True)
    idzona = models.ForeignKey('Zonas', blank=True, null=True)
    autor = models.ForeignKey('Autores', blank=True, null=True)
    autornota = RichTextField(blank=True, null=True)
    cambio = RichTextField(blank=True, null=True)
    texto = RichTextField(blank=True, null=True)
    codigoml = models.IntegerField(blank=True, null=True)
    nota = RichTextField(blank=True, null=True)
    temas = models.ManyToManyField(Temas, blank=True)

    def __unicode__(self):
        return self.titulo

    class Meta:
        db_table = 'articulos'
        verbose_name='Articulo'
        verbose_name_plural='Articulos'
        ordering = ['id']


# class Articulotemas(models.Model):
#     idarticulo = models.ForeignKey(Articulos, models.DO_NOTHING, db_column='idarticulo')
#     idtema = models.ForeignKey('Temas', models.DO_NOTHING, db_column='idtema')
#     ididioma = models.CharField(max_length=2, blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'articulotemas'
#         unique_together = (('idarticulo', 'idtema'),)

class Enlaces(models.Model):
    titulo = models.TextField(blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    idarticulo = models.ForeignKey(Articulos, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        db_table = 'enlaces'
        verbose_name='Enlace'
        verbose_name_plural='Enlaces'

class Tipo(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    tipo = models.CharField(max_length=500, blank=True, null=True)
    precio = models.CharField(max_length=50, blank=True, null=True)
    tipo_es = models.CharField(max_length=500, blank=True, null=True)
    tipo_en = models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return u'%s - %s' % (self.tipo, self.precio)

    class Meta:
        db_table = 'tipo'
        verbose_name='Tipo'
        verbose_name_plural='Tipos'


class Envio(models.Model):
    envio = models.CharField(max_length=500, blank=True, null=True)
    institucion = models.CharField(max_length=500, blank=True, null=True)
    direccion = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    apdo = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    idpais = models.CharField(max_length=2, blank=True, null=True)
    nueva = models.NullBooleanField()
    idioma = models.CharField(max_length=10, blank=True, null=True)
    forma_pago = models.CharField(max_length=2, blank=True, null=True)
    ttipo = models.CharField(max_length=4, blank=True, null=True)
    tnumero = models.CharField(max_length=50, blank=True, null=True)
    texpira = models.CharField(max_length=10, blank=True, null=True)
    tnombre = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=500, blank=True, null=True)
    idtipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='idtipo', blank=True, null=True)
    suscripcion = models.CharField(max_length=25, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.institucion

    class Meta:
        db_table = 'envio'
        verbose_name='Registro de subcriptores'
        verbose_name_plural='Registros de subcriptores'


class Pais(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    pais = models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.pais

    class Meta:
        db_table = 'pais'
        verbose_name='Pais'
        verbose_name_plural='Paises'
