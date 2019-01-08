from django.shortcuts import render
from departamentos.models import Departamentos
from disciplinas.forms import DisciplinaForm


def inicio(request):
    return  render(request, 'disciplinas/inicio.html', {
        'departamentos' : Departamentos.objects.all(),
        'form' : DisciplinaForm,
    })
