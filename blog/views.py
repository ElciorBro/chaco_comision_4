from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')


def nosotros(request):
    return render(request, 'nosotros.html', {
        "saludo": "Hola mundo",
        "nombre": "Soy el contexto",
        "autor": "Dani"
    })
    



# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         print("esto es el correo ingresado por el form login", email)
#         print("esto es el contraseña ingresado por el form login", password)

#     return render(request, 'usuarios/login.html')
