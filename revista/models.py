# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Idiomas(models.Model):
    idioma = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.idioma

    class Meta:
        verbose_name='idiomas'
        verbose_name_plural='idiomas'

class Zonas(models.Model):
    zona = models.CharField(max_length=50, blank=True, null=True)
    relevancia = models.IntegerField(blank=True, null=True)
    zona_en = models.CharField(max_length=50, blank=True, null=True)
    zona_es = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'zonas'

class Temas(models.Model):
    tema = models.CharField(max_length=150, blank=True, null=True)
    tema_en = models.CharField(max_length=150, blank=True, null=True)
    tema_es = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'temas'

class Autores(models.Model):
    nombre = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    titulo = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.TextField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)
    nombre_en = models.CharField(max_length=150, blank=True, null=True)
    nombre_es = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'autores'

class Revistas(models.Model):
    volumen = models.IntegerField()
    ano = models.IntegerField('Año', blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    ididioma = models.ForeignKey(Idiomas)
    nota = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return u'%s' % str(self.numero)

    class Meta:
        verbose_name='Revista'
        verbose_name_plural='Revistas'

class Articulos(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True)
    revista = models.ForeignKey(Revistas)
    idioma = models.ForeignKey(Idiomas, null=True, blank=True)
    idzona = models.ForeignKey('Zonas', blank=True, null=True)
    autor = models.ForeignKey('Autores', blank=True, null=True)
    autornota = models.TextField(blank=True, null=True)
    cambio = models.TextField(blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    codigoml = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)
    textoidx = models.TextField(blank=True, null=True)
    idxtexto = models.TextField(blank=True, null=True)
    temas = models.ManyToManyField(Temas, blank=True)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name='Articulos'
        verbose_name_plural='Articulos'


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

    class Meta:
        #managed = False
        db_table = 'enlaces'

class Tipo(models.Model):
    tipo = models.CharField(max_length=500, blank=True, null=True)
    precio = models.CharField(max_length=50, blank=True, null=True)
    tipo_es = models.CharField(max_length=500, blank=True, null=True)
    tipo_en = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'tipo'


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

    class Meta:
        #managed = False
        db_table = 'envio'


class Pais(models.Model):
    pais = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'pais'
