from django.forms import ModelForm, Textarea
from ckeditor.widgets import CKEditorWidget
from .models import Articulos

class ArticulosAdminForm(ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'
