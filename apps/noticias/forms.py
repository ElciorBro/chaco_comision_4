from django import forms
from .models import Contacto, Noticia


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'fecha', 'imagen', 'categoria_noticia']
        