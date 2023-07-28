"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# importamos include para poder trabajar con las urls de noticias
from django.urls import path, include
# from apps.noticias import views
from . import views

# url del login
from django.contrib.auth import views as auth
from django.conf.urls.static import static

from django.conf import settings

# URL PRINCIPAL
urlpatterns = [
    # path('', views.inicio, name="inicio"),
    path('admin/', admin.site.urls),
    # path para la url de la vista de home
    path('', views.home, name="home"),
    # path tiene 3 parametros direccion url, funcion de la vista(views),
    # path de nosotros
    path('nosotros/', views.nosotros, name="nosotros"),

    # ---------- URL APP NOTICIA-----------
    path('noticia/', include('apps.noticias.urls')),

    # LOGIN
    # path('usuarios/login', views.login, name='login')
    path('login/', auth.LoginView.as_view(template_name='noticias/login.html'), name='login'),
    # ultimo error de la clase solucionado
    # path('logout/', auth.LoginView.as_view(), name='logout'),
    # cambiar LoginView por LogoutView
    path('logout/', auth.LogoutView.as_view(), name='logout'),

    # Registro
    # path('usuarios/', include('apps.usuarios.urls')),
    
     #Mejores Juegos
    path("recomendaciones/", views.recomendaciones, name="recomendaciones")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
