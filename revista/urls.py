from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^revista/(?P<pk>[0-9]+)/$', views.revista_detail, name="revista-detail"),
    url(r'^lang/(?P<lang_code>\w+)/$', views.set_lang, name='set_lang'),
    url(r'^articulo/(?P<pk>[0-9]+)/$', views.DetailArticuloView.as_view(), name='articulo-detalle'),
    url(r'^busqueda-avanzada/$', views.busqueda, name="busqueda"),
    url(r'^busqueda/$', views.busqueda_avanzada, name="busqueda-avanzada"),
    #url(r'^busqueda/$', views.busqueda_google, name="googlesearch-results"),
    url(r'^archivos/$', views.archivos_revista, name="archivos"),
    url(r'^archivos/(?P<yearr>[0-9]+)/$', views.archivos_revista, name="archivos"),
    url(r'^subcribase/$', views.suscribete, name="suscribete"),
    url(r'^busqueda-por-tema/(?P<pk>[0-9]+)/$', views.articulo_busqueda_tema, name="tema"),
    url(r'^busqueda-por-zona/(?P<pk>\w+)/$', views.articulo_busqueda_zona, name="zona"),
    url(r'^busqueda-por-autor/(?P<pk>[0-9]+)/$', views.articulo_busqueda_autor, name="autor"),

]
