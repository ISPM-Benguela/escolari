from django.shortcuts import render, HttpResponse
from departamentos.models import Departamentos
from anolectivo.models import AnoLectivo
from anolectivo.forms import AnolectivoForm

def inicio(request):
    contexto = {
        'departamentos' : Departamentos.objects.all(),
        'anolectivo' : AnoLectivo.objects.all(),
        'form' : AnolectivoForm,
    }
    return render(request, 'ano/inicio.html', contexto)