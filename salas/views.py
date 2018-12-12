from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from departamentos.models import Departamentos
from salas.models import Turmas

def todos(request):
    turmas = Turmas.objects.all()
    return render(request, 'turmas/index.html', {
        'departamentos': Departamentos.objects.all(),
        'turmas' : turmas,
    })