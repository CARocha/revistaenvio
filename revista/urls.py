from django.conf.urls import url
from .views import IndexView, DetailArticuloView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^articulo/(?P<pk>[0-9]+)/$', DetailArticuloView.as_view(), name='articulo-detalle'),
]
