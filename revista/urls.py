from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^lang/(?P<lang_code>\w+)/$', views.set_lang, name='set_lang'),
    url(r'^articulo/(?P<pk>[0-9]+)/$', views.DetailArticuloView.as_view(), name='articulo-detalle'),
    #url(r'^busqueda/$', views.busqueda, name="busqueda"),
    #url(r'^busqueda/$', views.busqueda_google, name="googlesearch-results"),
    url(r'^archivos/$', views.archivos_revista, name="archivos"),
    url(r'^archivos/(?P<yearr>[0-9]+)/$', views.archivos_revista, name="archivos"),

]
