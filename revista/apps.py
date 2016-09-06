from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson
#from revista.models import Articulos


class RevistaConfig(AppConfig):
    name = 'revista'
    def ready(self):
		modelo = self.get_model("Articulos")
		watson.register(modelo)
