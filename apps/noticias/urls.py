from django.urls import path
from . import views

app_name = 'noticias'

# Urls de app noticias
urlpatterns = [

    path('', views.inicio, name="inicio"),

    # url para el detalle de la noticia por pk
    path('detalle/<int:pk>/', views.Detalle_Noticias, name='detalle'),

    # url del formulario de contacto
    path('contacto', views.Contact.as_view(), name="contacto"),

    # URL COMENTARIO
    path('comentario', views.Comentar_Noticia, name='comentar'),
    
    # crear noti
    path('registrar_noticia/', views.CrearNoticia.as_view(), name='registrar_noticia'),

    # Registro de Usuarios
    path('registro/', views.Registro.as_view(), name="registro"),
    
    path('editar/<int:pk>/', views.editar_noticia, name='editar_noticia'),

    path('borrar/<int:pk>/', views.borrar_noticia, name='borrar_noticia'),
]

