from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    p1 = Persona('Profesor Freddy', 'Portales')
    nombre = 'Freddy'
    apellido = 'Portales'
    today = datetime.datetime.now()
    temas_del_curso = ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    # temas_del_curso = []
    # doc_externo = open('proyecto1/templates/miplantilla.html')
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    # doc_externo = get_template('miplantilla.html')

    # ctx = Context({
    #     'nombre_persona': nombre,
    #     'apellido_persona': apellido,
    #     'momento_actual': today,
    #     'persona': p1,
    #     'temas': temas_del_curso
    # })

    ctx = {
        'nombre_persona': nombre,
        'apellido_persona': apellido,
        'momento_actual': today,
        'persona': p1,
        'temas': temas_del_curso
    }
    # documento = plt.render(ctx)
    # documento = doc_externo.render(ctx)
    return render(request, 'miplantilla.html', ctx)


def despedida(request):
    return HttpResponse('Hasta luego alumnos de Django')


def dame_fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
        <html>
            <body>
                <h2>Fecha y hora actuales %s</h2>
            </body>
        </html>""" % fecha_actual
    return HttpResponse(documento)


def calcula_edad(request, anio, edad):
    periodo = anio - 2019
    edad_futura = edad + periodo
    documento = """
        <html>
            <body>
                <h2>En el año %s tendrás %s</h2>
            </body>
        </html>""" % (anio, edad_futura)
    return HttpResponse(documento)


def curso_c(request):
    fecha_actual = datetime.datetime.now()
    context = {
        'dame_fecha': fecha_actual,
        'nombre': 'Freddy',
    }
    return render(request, 'cursoC.html', context)


def curso_css(request):
    fecha_actual = datetime.datetime.now()
    context = {
        'dame_fecha': fecha_actual,
        'nombre': 'Freddy',
    }
    return render(request, 'cursoCss.html', context)

