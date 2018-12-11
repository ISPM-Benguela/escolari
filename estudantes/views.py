from django.shortcuts import render
from departamentos.models import Departamentos

def inicio(request):
    contexto = {
        'departamentos' : Departamentos.objects.all(),
    }
    return render(request, 'estudantes/inicio.html', contexto)