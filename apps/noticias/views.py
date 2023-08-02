# dependencias de Django
from django.shortcuts import render, HttpResponse, redirect
# Importacion de Modelos
from .models import Noticia, Categoria, Contacto, Comentario
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
        form = RegistroForm()  # Utiliza tu formulario personalizado
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)  # Utiliza tu formulario personalizado
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




# uso de decorador para verificar logeo de usuario y poder ver noticia
@login_required
def inicio(request):
    # obtener todas las noticias y mostrar en el inicio.html
    # ctx = {}
    # # clase.objetcs.all()==> select * from noticia
    # noticia = Noticia.objects.all()
    # ctx["noticias"] = noticia
    # return render(request, 'noticias/inicio.html', ctx)
    contexto = {}
    id_categoria = request.GET.get('id', None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        n = Noticia.objects.all()  # una lista

    contexto['noticias'] = n

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
        return redirect('noticias:inicio')  # Redirige a la página de inicio después de borrar la noticia

    return render(request, 'noticias/borrar.html', {'noticia': noticia})




#Formulario de Registro de noticas
# @login_required
# def registrar_noticia(request):
#     data = {
#         'form': NoticiaForm()
#     }
#     if request.method == 'POST':
#         formulario = NoticiaForm(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('home')
#     else:
#         formulario = NoticiaForm()
        
#     return render(request, 'noticias/registrar_noticia.html', data)

class CrearNoticia(LoginRequiredMixin, CreateView):
	model = Noticia
	form_class = NoticiaForm
	template_name = 'noticias/registrar_noticia.html'
	success_url = reverse_lazy('noticias:inicio')
	
	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		return super(CrearNoticia, self).form_valid(form)

# ClaseName.objects.all()[0:2]              select * from noticias
# ClaseName.objects.get(pk = 1)        select * from noticias where id = 1
# ClaseName.objects.filter(categoria)  select * from noticias where categoria = deportes



def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        ContactoForm(data=request.POST).save()

    return render(request, 'contacto/formulario.html', data)


@login_required
def Comentar_Noticia(request):
    comentario = request.POST.get('comentario', None)
    user = request.user
    noti = request.POST.get('id_noticia', None)
    noticia = Noticia.objects.get(pk=noti)
    coment = Comentario.objects.create(
        usuario=user, noticia=noticia, texto=comentario)
    return redirect(reverse_lazy('noticias:detalle', kwargs={"pk": noti}))


