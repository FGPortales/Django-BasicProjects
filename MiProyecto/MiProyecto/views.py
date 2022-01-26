from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render
from django.template import Template, Context
# from django.template import loader
from django.template.loader import get_template


#  Request: Para realizar peticiones
#  HttpResponse: Para enviar la respuesta usando el protocolo HTTP

#  Esto es una vista


def bienvenida(request):  # Pasamos un objeto de tipo request como primer argumento
    return HttpResponse('Bienvenido a este curso de Django')


def bienvenida_rojo(request):  # Pasamos un objeto de tipo request como primer argumento
    return HttpResponse('<p style="color: red">Bienvenido a este curso de Django</p>')


def categoria_edad(request, age):
    if age >= 18:
        if age >= 60:
            categoria = 'Tercera edad'
        else:
            categoria = 'Adultez'
    else:
        if age < 10:
            categoria = 'Infancia'
        else:
            categoria = 'Adolescencia'
    resultado = '<h1>Categoria de la edad: %s</h1>' % categoria
    return HttpResponse(resultado)


def get_today(request):
    result = f"<h1>la fecha actual es: {datetime.now().strftime('%d/%m/%Y - %X')}</h1>"
    return HttpResponse(result)


def contenido_html(request, nombre, edad):
    contenido = """
    <html>
        <body>
            <p>Nombre: %s / Edad: %s</p>
        </body>
    </html>
    """ % (nombre, edad)
    return HttpResponse(contenido)


def mi_primera_plantilla(request):
    plantilla_externa = open('MiProyecto/plantillas/miPrimeraPlantilla.html')
    # Cargar un documento en una variable de tipo 'Template'
    template = Template(plantilla_externa.read())
    plantilla_externa.close()
    # Crea contexto
    contexto = Context()
    # Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)


def plantilla_parametros(request):
    nombre = 'freddygpa'
    fecha_actual = datetime.now()
    programming_languages = ['python', 'c++', 'dart', 'java', 'php', 'ruby', 'javascript']
    plantilla_externa = open('MiProyecto/plantillas/plantilla_parametro.html')
    template = Template(plantilla_externa.read())
    plantilla_externa.close()
    context = Context({'nombre': nombre, 'date': fecha_actual, 'languages': programming_languages})
    documento = template.render(context)
    return HttpResponse(documento)


def plantilla_cargador(request):
    nombre = 'freddygpa'
    fecha_actual = datetime.now()
    programming_languages = ['python', 'c++', 'dart', 'java', 'php', 'c#', 'ruby', 'javascript']
    # Especificando la carpeta donde se encuentra la plantilla y creamos una variable que la almacena
    # plantilla_externa = loader.get_template('plantilla_parametro.html')
    plantilla_externa = get_template('plantilla_parametro.html')
    # Renderizar el documento:
    documento = plantilla_externa.render({'nombre': nombre, 'date': fecha_actual, 'languages': programming_languages})
    return HttpResponse(documento)


def plantilla_shortcut(request):
    nombre = 'freddygpa'
    fecha_actual = datetime.now()
    programming_languages = ['python', 'c++', 'dart', 'java', 'php', 'c#', 'c', 'ruby', 'javascript']
    return render(request, 'plantilla_parametro.html', {'nombre': nombre, 'date': fecha_actual, 'languages': programming_languages})


def plantilla_hija1(request):
    return render(request, 'plantilla_hija1.html', {})


def plantilla_hija2(request):
    return render(request, 'plantilla_hija2.html', {})
