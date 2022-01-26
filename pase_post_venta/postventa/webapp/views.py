from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from clientes.models import Cliente, Marca, Categoria, Acceso, Equipo


def bienvenido(request):
    return render(request, 'bienvenido.html', {})


def Clientes(request):
    context = {
        'num_cli': Cliente.objects.count(),
        'my_clients': Cliente.objects.order_by('id')  # Cliente.objects.all()
    }
    return render(request, 'clientes.html', context)


def equipo(request):
    context = {
        'num_devices': Equipo.objects.count(),
        'devices': Equipo.objects.order_by('id')
    }
    return render(request, 'device.html', context)


def marca(request):
    context = {
        'num_marcas': Marca.objects.count(),
        'marcas': Marca.objects.order_by('id')
    }
    return render(request, 'marca.html', context)


def categoria(request):
    context = {
        'num_categorias': Categoria.objects.count(),
        'categorias': Categoria.objects.order_by('id')
    }
    return render(request, 'categoria.html', context)


def acceso(request):
    context = {
        'num_accesos': Acceso.objects.count(),
        'accesos': Acceso.objects.order_by('id')
    }
    return render(request, 'acceso.html', context)


def despedirse(request):
    return HttpResponse('Despedida desde Django')


def contacto(request):
    return HttpResponse('Teléfono: 9991121213\nEmail: freddy@gmail.com')