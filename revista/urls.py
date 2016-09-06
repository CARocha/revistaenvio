from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^articulo/(?P<pk>[0-9]+)/$', views.DetailArticuloView.as_view(), name='articulo-detalle'),
    url(r'^busqueda/$', views.busqueda, name="busqueda"),

]
