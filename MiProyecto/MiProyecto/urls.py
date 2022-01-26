"""MiProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from MiProyecto.views import bienvenida, bienvenida_rojo, categoria_edad, get_today, contenido_html, \
    mi_primera_plantilla, plantilla_parametros, plantilla_cargador, plantilla_shortcut, plantilla_hija1, plantilla_hija2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('bienvenida_rojo/', bienvenida_rojo),
    path('categoria_age/<int:age>', categoria_edad),
    path('today/', get_today),
    path('contenido/<nombre>/<int:edad>', contenido_html),
    path('plantilla/', mi_primera_plantilla),
    path('parametro/', plantilla_parametros),
    path('plantilla_cargador/', plantilla_cargador),
    path('plantilla_shortcut/', plantilla_shortcut),
    path('plantilla_hija1/', plantilla_hija1),
    path('plantilla_hija2/', plantilla_hija2),
]
