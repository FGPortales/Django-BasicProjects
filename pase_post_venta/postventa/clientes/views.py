from django.forms import modelform_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import View

from clientes.forms import ClienteForm, MarcaForm, CategoriaForm, AccesoForm, EquipoForm
from clientes.models import Cliente


def detalle_cliente(request, id_cliente):
    client = get_object_or_404(Cliente, pk=id_cliente)
    return render(request, 'detalle.html', {'cliente_dic': client})


# ClienteForm = modelform_factory(Cliente, exclude=[])


def nuevo_cliente(request):
    if request.method == 'POST':
        forma_cliente = ClienteForm(request.POST)
        if forma_cliente.is_valid():
            forma_cliente.save()
            return redirect('inicio')
    else:
        forma_cliente = ClienteForm()
    return render(request, 'nuevo.html', {'formaCliente': forma_cliente})


def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    if request.method == 'POST':
        forma_cliente = ClienteForm(request.POST, instance=cliente)
        if forma_cliente.is_valid():
            forma_cliente.save()
            return redirect('inicio')
    else:
        forma_cliente = ClienteForm(instance=cliente)
    return render(request, 'editar.html', {'formaCliente': forma_cliente})


def eliminar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    if cliente:
        cliente.delete()
    return redirect('inicio')


def nuevo_equipo(request):
    if request.method == 'POST':
        forma_equipo = EquipoForm(request.POST)
        if forma_equipo.is_valid():
            forma_equipo.save()
            return redirect('equipo')
    else:
        forma_equipo = EquipoForm()
    return render(request, 'nuevo_equipo.html', {'formaEquipo': forma_equipo})


def nueva_marca(request):
    if request.method == 'POST':
        forma_marca = MarcaForm(request.POST)
        if forma_marca.is_valid():
            forma_marca.save()
            return redirect('marca')
    else:
        forma_marca = MarcaForm()
    return render(request, 'nueva_marca.html', {'formaMarca': forma_marca})


def nueva_categoria(request):
    if request.method == 'POST':
        forma_categoria = CategoriaForm(request.POST)
        if forma_categoria.is_valid():
            forma_categoria.save()
            return redirect('categoria')
    else:
        forma_categoria = CategoriaForm()
    return render(request, 'nueva_categoria.html', {'formaCategoria': forma_categoria})


def nuevo_acceso(request):
    if request.method == 'POST':
        forma_acceso = AccesoForm(request.POST)
        if forma_acceso.is_valid():
            forma_acceso.save()
            return redirect('acceso')
    else:
        forma_acceso = AccesoForm()
    return render(request, 'nueva_acceso.html', {'formaAcceso': forma_acceso})


class PartnersListView(View):
    def get(self, request):
        clientes_list = Cliente.objects.all()
        return JsonResponse(list(clientes_list.values()), safe=False)
