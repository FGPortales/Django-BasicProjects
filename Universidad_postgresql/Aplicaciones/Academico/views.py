from django.shortcuts import render
from .models import Curso
from django.views.generic import ListView
# from django.http import HttpResponse

# Create your views here.


# def home(request):
#     cursosListado = Curso.objects.all()
#     # cursosListado = Curso.objects.all()[:3]
#     # cursosListado = Curso.objects.all().order_by('nombre')  # Ordena por nombre de forma ascendente
#     # cursosListado = Curso.objects.all().order_by('-nombre')  # Ordena por nombre de forma descendente
#     # cursosListado = Curso.objects.all().order_by('nombre', 'creditos')  # dos criterios para el ordenamiento
#     # cursosListado = Curso.objects.filter(nombre='Física')  # Filtra por nombre
#     # cursosListado = Curso.objects.filter(creditos__gte=5)  # Filtra por créditos mayor que 5
#     # cursosListado = Curso.objects.filter(creditos__lte=5)  # Filtra por créditos menor que 5
#     # cursosListado = Curso.objects.filter(nombre__startswith='A')
#     # cursosListado = Curso.objects.filter(nombre__contains='g')
#     # return HttpResponse("<h1>Hola mundo</h1>")
#     context = {
#         'titulo': 'Gestión de Cursos',
#         'cursos': cursosListado
#     }
#     # return render(request, 'gestionCurso.html', {'cursos': cursosListado})
#     return render(request, 'gestionCurso.html', context)


class CursoListView(ListView):
    """ Vista basada en clases"""
    model = Curso
    template_name = 'gestionCurso.html'

    def get_queryset(self):
        # return Curso.objects.all()
        return Curso.objects.filter(creditos__lte=4)

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context.update({'titulo': 'Gestión de Cursos'})
        return context
