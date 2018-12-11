from django.shortcuts import render
from departamentos.models import Departamentos
from estudantes.forms import EstudanteForm

def inicio(request):
    contexto = {
        'departamentos' : Departamentos.objects.all(),
        'form' : EstudanteForm,
    }
    return render(request, 'estudantes/inicio.html', contexto)