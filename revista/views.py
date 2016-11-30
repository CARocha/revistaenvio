# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, DetailView, ListView
from django.utils import translation
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import *
from .forms import SubcribeteForm, BusquedaAvanzada
import datetime

def set_lang(request, lang_code):
    if not lang_code in ['en', 'es']:
        raise Http404

    next = request.GET.get('next', '/')
    if not next:
        next = request.META.get('HTTP_REFERER', '/')
    response = HttpResponseRedirect(next)

    if hasattr(request, 'session'):
        request.session['django_language'] = lang_code
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)

    return response

class IndexView(ListView):
    template_name = "index.html"
    model = Revistas
    paginate_by = 1

    def get_queryset(self):
        cur_language = translation.get_language()
        if cur_language == 'en':
            queryset = Revistas.objects.filter(ididioma='en').order_by('-numero')
        else:
            queryset = Revistas.objects.filter(ididioma='es').order_by('-numero')
        return queryset

def revista_detail(request, pk=None, template='index.html'):
    object_list = Revistas.objects.filter(id=pk);

    return render(request, template, locals())


class DetailArticuloView(DetailView):
    model = Articulos

    def get_context_data(self, **kwargs):
        context = super(DetailArticuloView, self).get_context_data(**kwargs)
        revista = Revistas.objects.get(id=self.object.revista_id)
        context['ultima_revista'] = revista
        context['articulos'] = Articulos.objects.filter(revista_id=revista).exclude(id=self.object.id)
        return context


def busqueda(request, template='revista/busqueda_avanzada.html'):
    cur_language = translation.get_language()
    if cur_language == 'en':
        all_temas = Temas.objects.all()
        all_zonas = Zonas.objects.all()
        all_autores = Autores.objects.all()
    else:
        all_temas = Temas.objects.all()
        all_zonas = Zonas.objects.all()
        all_autores = Autores.objects.all()

    form = BusquedaAvanzada()

    return render(request, template, locals())


def archivos_revista(request, template='revista/archivos.html', yearr=None):
    cur_language = translation.get_language()
    if cur_language == 'en':
        years = []
        for en in Revistas.objects.filter(ididioma='en').order_by('-ano').values_list('ano', flat=True):
            years.append((en,en))
        all_year1 = list(sorted(set(years)))
        idioma = 'en'
    else:
        years = []
        for en in Revistas.objects.filter(ididioma='es').order_by('-ano').values_list('ano', flat=True):
            years.append((en,en))
        all_year1 = list(sorted(set(years)))
        idioma = 'es'

    if yearr is None:
            now = datetime.datetime.now()
            query = Revistas.objects.filter(ididioma=idioma,ano=now.year).order_by('-mes')
    else:
            query = Revistas.objects.filter(ano=yearr,ididioma=idioma).order_by('-numero')

    return render(request, template, locals())


def suscribete(request, template='revista/suscribete.html'):

    form = SubcribeteForm()
    return render(request, template, locals())

def articulo_busqueda_tema(request, pk=None, template='revista/por_tema.html'):
    cur_language = translation.get_language()
    tema_buscado = Temas.objects.get(id=pk)
    if cur_language == 'en':
        temas_articulos = Articulos.objects.filter(idioma='en', temas=pk);
    else:
         temas_articulos = Articulos.objects.filter(idioma='es', temas=pk);

    paginator = Paginator(temas_articulos, 10)

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    return render(request, template, locals())

def articulo_busqueda_zona(request, pk=None, template='revista/por_zona.html'):
    cur_language = translation.get_language()
    if cur_language == 'en':
        zonas_articulos = Articulos.objects.filter(idioma='en', idzona=pk);
    else:
         zonas_articulos = Articulos.objects.filter(idioma='es', idzona=pk);

    paginator = Paginator(zonas_articulos, 10)

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    return render(request, template, locals())

def articulo_busqueda_autor(request, pk=None, template='revista/por_autor.html'):
    cur_language = translation.get_language()
    if cur_language == 'en':
        autor_articulos = Articulos.objects.filter(idioma='en', autor=pk);
    else:
         autor_articulos = Articulos.objects.filter(idioma='es', autor=pk);

    paginator = Paginator(autor_articulos, 10)

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    return render(request, template, locals())


def busqueda_avanzada(request, template='revista/busqueda_mega_avanzada.html'):
    params = {}
    if request.method == 'POST':
        params['revista__mes__gte'] = request.POST.get('mes_1')
        params['revista__ano__gte'] = request.POST.get('year_1')
        params['revista__mes__lte'] = request.POST.get('mes_2')
        params['revista__ano__lte'] = request.POST.get('year_2')
        params['idzona'] = request.POST.get('zona')
        params['temas__in'] = request.POST.get('temas')
        params['titulo'] = request.POST.get('buscar')

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]
        
    object_list = Articulos.objects.filter(**params)
    #Articulos.objects.filter(revista__ano__gte=2015,revista__ano__lte=2016, revista__mes__gte=1, revista__mes__lte=2)
    print len(object_list)
    print "---- arriba imprimio----"

    return render(request, template, locals())