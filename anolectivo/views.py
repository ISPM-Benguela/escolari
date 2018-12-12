from django.shortcuts import render, HttpResponse
from departamentos.models import Departamentos

def inicio(request):
    contexto = {
        'departamentos' : Departamentos.objects.all(),
    }
    return render(request, 'ano/inicio.html', contexto)