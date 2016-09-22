# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from revista.models import Revistas

class LatestRevistaFeed(Feed):
    title = "Revista Envío"
    link = "/index/"
    description = "Actualización estas son las ultimas revistas"

    def items(self):
        return Revistas.objects.order_by('-numero')[:5]

    def item_title(self, item):
        return str(item.numero)

    def item_description(self, item):
        return str(item.ano)

    # item_link is only needed if Revistas has no get_absolute_url method.
    def item_link(self, item):
        return reverse('revista-detail', args=[item.pk])