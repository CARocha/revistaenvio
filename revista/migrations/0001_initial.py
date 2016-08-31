# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True)),
                ('autornota', models.TextField(blank=True, null=True)),
                ('cambio', models.TextField(blank=True, null=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('codigoml', models.IntegerField(blank=True, null=True)),
                ('nota', models.TextField(blank=True, null=True)),
                ('textoidx', models.TextField(blank=True, null=True)),
                ('idxtexto', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'articulos',
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
        ),
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo', models.TextField(blank=True, null=True)),
                ('nota', models.TextField(blank=True, null=True)),
                ('nombre_en', models.CharField(blank=True, max_length=150, null=True)),
                ('nombre_es', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'autores',
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Enlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(blank=True, null=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('idarticulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revista.Articulos')),
            ],
            options={
                'db_table': 'enlaces',
                'verbose_name': 'Enlace',
                'verbose_name_plural': 'Enlaces',
            },
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('envio', models.CharField(blank=True, max_length=500, null=True)),
                ('institucion', models.CharField(blank=True, max_length=500, null=True)),
                ('direccion', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('apdo', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo', models.CharField(blank=True, max_length=50, null=True)),
                ('idpais', models.CharField(blank=True, max_length=2, null=True)),
                ('nueva', models.NullBooleanField()),
                ('idioma', models.CharField(blank=True, max_length=10, null=True)),
                ('forma_pago', models.CharField(blank=True, max_length=2, null=True)),
                ('ttipo', models.CharField(blank=True, max_length=4, null=True)),
                ('tnumero', models.CharField(blank=True, max_length=50, null=True)),
                ('texpira', models.CharField(blank=True, max_length=10, null=True)),
                ('tnombre', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('suscripcion', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'envio',
                'verbose_name': 'Registro de subcriptores',
                'verbose_name_plural': 'Registros de subcriptores',
            },
        ),
        migrations.CreateModel(
            name='Idiomas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'idiomas',
                'verbose_name': 'Idioma',
                'verbose_name_plural': 'Idiomas',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('pais', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'pais',
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Revistas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volumen', models.IntegerField()),
                ('ano', models.IntegerField(blank=True, null=True, verbose_name='A\xf1o')),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('nota', models.TextField(blank=True, null=True)),
                ('color', models.IntegerField(blank=True, null=True)),
                ('ididioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revista.Idiomas')),
            ],
            options={
                'db_table': 'revistas',
                'verbose_name': 'Revista',
                'verbose_name_plural': 'Revistas',
            },
        ),
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(blank=True, max_length=150, null=True)),
                ('tema_en', models.CharField(blank=True, max_length=150, null=True)),
                ('tema_es', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'temas',
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=500, null=True)),
                ('precio', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_es', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo_en', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'tipo',
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='Zonas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(blank=True, max_length=50, null=True)),
                ('relevancia', models.IntegerField(blank=True, null=True)),
                ('zona_en', models.CharField(blank=True, max_length=50, null=True)),
                ('zona_es', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'zonas',
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
            },
        ),
        migrations.AddField(
            model_name='envio',
            name='idtipo',
            field=models.ForeignKey(blank=True, db_column='idtipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='revista.Tipo'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revista.Autores'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='idioma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revista.Idiomas'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='idzona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revista.Zonas'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='revista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revista.Revistas'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='temas',
            field=models.ManyToManyField(blank=True, to='revista.Temas'),
        ),
    ]
