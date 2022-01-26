"""sap URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from clientes.views import detalle_cliente, nuevo_cliente, editar_cliente, eliminar_cliente, nueva_marca, \
    nueva_categoria, nuevo_acceso, nuevo_equipo
from webapp.views import despedirse, contacto, marca, Clientes, bienvenido, categoria, acceso, equipo

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bienvenido/', bienvenido),
    path('', bienvenido),
    path('clientes', Clientes, name='inicio'),  # , name='inicio'
    path('equipo/', equipo, name='equipo'),
    path('marca/', marca, name='marca'),
    path('categoria/', categoria, name='categoria'),
    path('acceso/', acceso, name='acceso'),
    path('despedida.html', despedirse),
    path('contact_user', contacto),
    path('detalle_cli/<int:id_cliente>', detalle_cliente),
    path('editar_cli/<int:id_cliente>', editar_cliente),
    path('eliminar_cli/<int:id_cliente>', eliminar_cliente),
    path('nuevo_cliente', nuevo_cliente),
    path('equipo/nuevo_equipo', nuevo_equipo),
    path('marca/nueva_marca', nueva_marca),
    path('acceso/nuevo_acceso', nuevo_acceso),
    path('categoria/nueva_categoria', nueva_categoria),
    path('api/', include('clientes.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
