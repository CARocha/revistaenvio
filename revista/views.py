# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.utils import translation
from .models import *

def set_lang(request, lang_code):
    if not lang_code in ['en', 'es']:
        raise Http404

    next = request.GET.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', '/')
    response = HttpResponseRedirect(next)

    if hasattr(request, 'session'):
        request.session['django_language'] = lang_code
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)

    return response

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        cur_language = translation.get_language()
        if cur_language == 'en':
            en_revista = Revistas.objects.filter(ididioma='en').latest('numero')
            context['ultima_revista'] = en_revista
            context['todos_articulos'] = Articulos.objects.filter(revista=en_revista).order_by('id')
        else:
            es_revista = Revistas.objects.filter(ididioma='es').latest('numero')
            context['ultima_revista'] = es_revista
            context['todos_articulos'] = Articulos.objects.filter(revista=es_revista).order_by('id')
        return context

class DetailArticuloView(DetailView):
    model = Articulos


def busqueda(request, template='revista/busqueda_avanzada.html'):
    

    return render(request, template, locals())