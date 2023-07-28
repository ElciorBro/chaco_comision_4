from django.urls import path
from . import views

app_name = 'noticias'

# Urls de app noticias
urlpatterns = [

    path('', views.inicio, name="inicio"),

    # url para el detalle de la noticia por pk
    path('detalle/<int:pk>/', views.Detalle_Noticias, name='detalle'),

    # url del formulario de contacto
    path('contacto', views.contacto, name="contacto"),

    # URL COMENTARIO
    path('comentario', views.Comentar_Noticia, name='comentar'),
    
    # URL de registracion de noticias
    # path('registrar_noticia/', views.registrar_noticia, name='registrar_noticia'),

    # crear noti
    path('registrar_noticia/', views.CrearNoticia.as_view(), name='registrar_noticia'),

    # Registro de Usuarios
    path('registro/', views.Registro.as_view(), name="registro"),
    
   
    
]
