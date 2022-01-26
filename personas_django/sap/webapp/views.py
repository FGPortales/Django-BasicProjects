from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    num_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {'num_personas': num_personas, 'personas': personas})
