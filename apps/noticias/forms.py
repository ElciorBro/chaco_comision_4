from django import forms
from .models import Contacto, Noticia


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'imagen', 'categoria_noticia']

class BuscadorForm(forms.Form):
    busqueda = forms.CharField(label='Buscar', max_length=100)
