from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.
from gestionPedidos.models import Articulos


def busqueda_producto(request):
    return render(request, 'busqueda_productos.html')


def busqueda(request):
    if request.GET['productox']:
        # mensaje = 'Artículo buscado: %s' % request.GET['producto']
        product = request.GET['productox']
        if len(product) > 20:
            mensaje = 'Texto de busqueda demasiado largo.'
        else:
            articulos = Articulos.objects.filter(nombre__icontains=product)  # Realiza una busqueda en BD por 'nombre'
            return render(request, 'resultado_busqueda.html', {'articulos': articulos, 'query': product})
    else:
        mensaje = 'No has introducido nada'
    return HttpResponse(mensaje)


# def contacto(request):
#     if request.method == 'POST':
#         subject = request.POST['asunto']
#         mensaje = request.POST['mensaje'] + ' ' + request.POST['email']
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = ['freddy9.40g@gmail.com']
#         send_mail(subject, mensaje, email_from, recipient_list)
#         html = 'gracias.html'
#     else:
#         html = 'contacto.html'
#     return render(request, html)

def contacto(request):
    if request.method == 'POST':
        my_form = FormularioContacto(request.POST)
        ctx = {}
        if my_form.is_valid():
            data_form = my_form.cleaned_data
            send_mail(data_form['asunto'], data_form['mensaje'], data_form['email'], ['freddy9.40g@gmail.com'])
            html = 'gracias.html'
    else:
        my_form = FormularioContacto()
        html = 'formulario_contacto.html'
        ctx = {'form': my_form}
    return render(request, html, ctx)
