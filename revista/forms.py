# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea
from ckeditor.widgets import CKEditorWidget
from .models import Articulos, Envio, Temas, Zonas, CHOICES_MES, Revistas
from django.utils import translation

class ArticulosAdminForm(ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'

class SubcribeteForm(ModelForm):
    class Meta:
        model = Envio
        fields = '__all__'


# def choice_year():
#     cur_language = translation.get_language()
#     all_year1 = []
#     if cur_language == 'en':
#         years = []
#         for en in Revistas.objects.filter(ididioma='en').order_by('-ano').values_list('ano', flat=True):
#             years.append((en,en))
#         all_year1 = list(sorted(set(years)))
#     else:
#         years = []
#         for en in Revistas.objects.filter(ididioma='es').order_by('-ano').values_list('ano', flat=True):
#             years.append((en,en))
#         all_year1 = list(sorted(set(years)))
#     return all_year1
choice_year = ((1,'uno'),(2,'dos'),)

class BusquedaAvanzada(forms.Form):
    #------- inicio --------------
    mes_1 = forms.ChoiceField(choices=CHOICES_MES)
    year_1 = forms.ChoiceField(choices=choice_year)
    #-------- fin ----------------
    mes_2 = forms.ChoiceField(choices=CHOICES_MES)
    year_2 = forms.ChoiceField(choices=choice_year)
    #------- zona ---------------
    zona = forms.ModelMultipleChoiceField(queryset=Zonas.objects.all(), required=False)
    temas = forms.ModelMultipleChoiceField(queryset=Temas.objects.all(), required=False)
    #----- input busqueda ---------
    buscar = forms.CharField(max_length=250)
