# dependencias de Django
from django.shortcuts import render, HttpResponse, redirect
# Importacion de Modelos
from .models import Noticia, Categoria, Comentario, Contacto
#importacion de Formularios
from .forms import NoticiaForm, ContactoForm, RegistroForm
# importamos reverse lazy para los comentarios
from django.urls import reverse_lazy
# importacion del decorador para verificar logueo
from django.contrib.auth.decorators import login_required
# Clase mixta para verificar que un usuario este logueado antes de ejecutar
from django.contrib.auth.mixins import LoginRequiredMixin
# Importacion de la dependencia para crear vistas en la BD 
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import LoginForm
from django.shortcuts import render, get_object_or_404, redirect

# Clases de Registro de Usuarios


class Registro(View):
    template_name = 'noticias/registro.html'

    def get(self, request):
        form = RegistroForm() 
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})


class Login(View):
    template_name = 'noticias/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Lógica para el inicio de sesión exitoso (opcional)
                return redirect('inicio')
        return render(request, self.template_name, {'form': form})




@login_required
def inicio(request):
    contexto = {}
    id_categoria = request.GET.get('id', None)
    orden = request.GET.get('orden', 'nuevas')  # Obtenemos el parámetro 'orden' de la URL o establecemos el valor predeterminado 'nuevas'

    if id_categoria:
        noticias = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        noticias = Noticia.objects.all()  # una lista

    if orden == 'nuevas':
        noticias = noticias.order_by('-fecha')  # Ordenamos por fecha más reciente (descendente)
    elif orden == 'viejas':
        noticias = noticias.order_by('fecha')  # Ordenamos por fecha más antigua (ascendente)
    elif orden == 'alf':
        noticias = noticias.order_by('titulo')  # Ordenamos alfabéticamente por título (ascendente)

    contexto['noticias'] = noticias

    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat

    return render(request, 'noticias/inicio.html', contexto)


@login_required
def Detalle_Noticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk)
    contexto['noticia'] = n

    c = Comentario.objects.filter(noticia=n)
    contexto['comentarios'] = c

    return render(request, 'noticias/detalle.html', contexto)

@login_required
def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias:detalle', pk=pk)
    else:
        form = NoticiaForm(instance=noticia)

    return render(request, 'noticias/editar.html', {'form': form, 'noticia': noticia})

@login_required
def borrar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    
    if request.method == 'POST':
        noticia.delete()
        return redirect('noticias:inicio')  

    return render(request, 'noticias/borrar.html', {'noticia': noticia})



class CrearNoticia(LoginRequiredMixin, CreateView):
	model = Noticia
	form_class = NoticiaForm
	template_name = 'noticias/registrar_noticia.html'
	success_url = reverse_lazy('noticias:inicio')
	
	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		return super(CrearNoticia, self).form_valid(form)




class Contact(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contacto/formulario.html'
    success_url = reverse_lazy('noticias:registrar_noticia')
    
    def form_valid(self, form):
        contacto = form.save(commit=False)
        return super(Contact, self).form_valid(form)


@login_required
def Comentar_Noticia(request):
    comentario = request.POST.get('comentario', None)
    user = request.user
    noti = request.POST.get('id_noticia', None)
    noticia = Noticia.objects.get(pk=noti)
    coment = Comentario.objects.create(
        usuario=user, noticia=noticia, texto=comentario)
    return redirect(reverse_lazy('noticias:detalle', kwargs={"pk": noti}))


