from django.shortcuts import render, HttpResponse
from departamentos.models import Departamentos

def inicio(request):
    return render(request, 'turmas/index.html', {
        'departamentos' : Departamentos.objects.all(),
    })
