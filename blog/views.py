from django.shortcuts import render, redirect
from apps.noticias.models import Noticia

def home(request):
    # Obtener las últimas 4 noticias ordenadas por fecha de publicación descendente
    noticias = Noticia.objects.order_by('-fecha')[:4]

    # Pasar las noticias al contexto
    context = {'noticia_0': noticias[0],
               'noticia_1': noticias[1],
               'noticia_2': noticias[2],
               'noticia_3': noticias[3]}
    
    return render(request, 'home.html', context)


def nosotros(request):
    return render(request, 'nosotros.html', {
        "saludo": "Hola mundo",
        "nombre": "Soy el contexto",
        "autor": "Dani"
    })
    
def recomendaciones(request):
    return render(request, "juegos.html")

