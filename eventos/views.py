from django.shortcuts import render
from departamentos.models import Departamentos
from eventos.models import Eventos

def todos(request):
    contexto = {
        'departamentos': Departamentos.objects.all(),
        'eventos' : Eventos.objects.all(),
    }
    return render(request, 'eventos/index.html', contexto)