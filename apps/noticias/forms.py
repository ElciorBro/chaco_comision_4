from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Contacto, Noticia, Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='apellido', required=True)
    password1 = forms.CharField(
        label='contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='contraseña2', widget=forms.PasswordInput, required=True)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']




class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'cuerpo', 'imagen', 'categoria_noticia')
        