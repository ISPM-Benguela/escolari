from django.shortcuts import render, HttpResponse
from departamentos.models import Departamentos

def inicio(request):
    return render(request, 'propinas/inicio.html',{
        'departamentos' : Departamentos.objects.all(),
    })

def pagar_propinas(request, nome):
    return HttpResponse(nome)