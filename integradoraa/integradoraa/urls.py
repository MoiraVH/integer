"""
URL configuration for integradoraa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from quickpass.views import home_view, auth_view, logout_view, profile_view, start_view

urlpatterns = [
    path('', start_view, name='root'),
    path('admin/', admin.site.urls),
    path('login/', auth_view, name='login'),  # ✅ Maneja login y registro
    path('logout/', logout_view, name='logout'),
    path('start/', start_view, name='start'),
    path('home/', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
]