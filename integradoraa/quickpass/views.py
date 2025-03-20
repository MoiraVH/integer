import re
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages as django_messages
from .models import UserModel


def auth_view(request):
    if request.method == "POST":
        if "login_submit" in request.POST:  # Inicio de sesión
            email = request.POST.get("email").strip()
            password = request.POST.get("password")

            user = UserModel.check_credentials(email, password)

            if user:
                request.session["user_id"] = str(user["_id"])
                request.session["name"] = user["name"]
                request.session["role"] = user["role"]  # Guardar el rol en la sesión
                django_messages.success(request, f"Bienvenido {user['name']}!")
                return redirect('home')
            else:
                django_messages.error(request, "Credenciales incorrectas.")


        elif "register_submit" in request.POST:  # Registro
            name = request.POST.get("name").strip()
            lastname = request.POST.get("lastname").strip()
            email = request.POST.get("email").strip()
            location = request.POST.get("location").strip()
            phone = request.POST.get("phone").strip()
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")

            # Validaciones
            if not name or not email or not password:
                django_messages.error(request, "Todos los campos son obligatorios.")
            elif UserModel.get_user_by_email(email):
                django_messages.error(request, "El correo ya está registrado.")
            elif password != confirm_password:
                django_messages.error(request, "Las contraseñas no coinciden.")
            elif len(password) < 6:
                django_messages.error(request, "La contraseña debe tener al menos 6 caracteres.")
            else:
            
                try:
                    user = UserModel(name, email, lastname, location, phone, password)
                    user.save()
                    django_messages.success(request, "Registro exitoso, ahora inicia sesión.")
                    return redirect("login")
                except Exception as e:
                    django_messages.error(request, f"Error al guardar el usuario: {e}")

    return render(request, "login.html")  # Renderizar plantilla de login con mensajes

def logout_view(request):
    """Cierra la sesión del usuario."""
    logout(request)
    django_messages.success(request, "Has cerrado sesión correctamente.")
    return redirect("login")

def home_view(request):
    return render(request, "home.html")


def start_view(request):
    return render(request, "start.html")

def profile_view(request):
    return render(request, "profile.html")

def profile_admin_view(request):
    return render(request, "profile_admin.html")

def about_us_view(request):
    return render(request, "about_us.html")

def admin_dashboard_view(request):
    return render(request, "admin_dashboard.html")