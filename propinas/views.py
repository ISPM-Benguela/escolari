from django.shortcuts import render
from departamentos.models import Departamentos

def inicio(request):
    return render(request, 'propinas/inicio.html',{
        'departamentos' : Departamentos.objects.all(),
    })
