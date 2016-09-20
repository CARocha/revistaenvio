from django.forms import ModelForm, Textarea
from ckeditor.widgets import CKEditorWidget
from .models import Articulos, Envio

class ArticulosAdminForm(ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'

class SubcribeteForm(ModelForm):
	class Meta:
		model = Envio
		fields = '__all__'

