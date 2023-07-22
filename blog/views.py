from django.shortcuts import render, redirect
from ..apps.noticias.models import Noticia
from ..apps.noticias.forms import NoticiasForm

def home(request):
    return render(request, 'home.html')


def nosotros(request):
    return render(request, 'nosotros.html', {
        "saludo": "Hola mundo",
        "nombre": "Soy el contexto",
        "autor": "Dani"
    })

def listado_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'blog/lista_noticias.html', {'noticias': noticias})

def detalles_noticias(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id)
    return render(request, 'blog/detalle_noticia.html', {'noticia': noticia})

def agregar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_noticias')
 
 

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         print("esto es el correo ingresado por el form login", email)
#         print("esto es el contraseña ingresado por el form login", password)

#     return render(request, 'usuarios/login.html')
