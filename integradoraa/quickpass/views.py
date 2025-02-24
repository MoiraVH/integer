from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages as django_messages
from .models import User

def auth_view(request):
    if request.method == "POST":
        # Verificamos qué formulario fue enviado
        if "login_submit" in request.POST:  # Botón de login
            email = request.POST['email']
            password = request.POST['password']
            
            if User.verify_password(email, password):
                request.session['user_email'] = email  # Guardar sesión
                django_messages.success(request, "Inicio de sesión exitoso")
                return redirect('home')
            else:
                django_messages.error(request, 'Credenciales inválidas')
                return redirect('login')  # Redirigir si falla el login

        elif "register_submit" in request.POST:  # Botón de registro
            name = request.POST['name']
            lastname = request.POST['lastname']
            email = request.POST['email']
            residencia = request.POST['location']
            number = request.POST['phone']
            password = request.POST['password']
            confirm_password = request.POST['confirmpass']

            if password != confirm_password:
                django_messages.error(request, "Las contraseñas no coinciden")
            elif User.get_by_email(email):
                django_messages.error(request, "El correo ya está registrado")
            else:
                user = User(name, lastname, email, residencia, number, password)
                user.save()
                django_messages.success(request, "Registro exitoso. ¡Ahora puedes iniciar sesión!")
                return redirect('login')

    return render(request, "login.html")  # Siempre renderizamos login.html

def logout_view(request):
    logout(request)
    django_messages.success(request, "Has cerrado sesión correctamente")
    return redirect('login')

def home_view(request):
    return render(request, "home.html")

def start_view(request):
    return render(request, "start.html")

def profile_view(request):
    return render(request, "profile.html")
