from django.shortcuts import render, HttpResponse
from departamentos.models import Departamentos
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from meses.models import Meses
from anolectivo.models import AnoLectivo

def inicio(request):
    return render(request, 'propinas/inicio.html',{
        'departamentos' : Departamentos.objects.all(),
    })

def pagar_propinas(request, nome):
    estudante = get_object_or_404(User, username=nome)

    return render(request, 'propinas/pagamentos.html',{
        'departamentos' : Departamentos.objects.all(),
        'estudante' : estudante,
        'meses': Meses.objects.all(),
        'anolectivos': AnoLectivo.objects.all(),
    })

def cadastrar_pagamento(request):
    return HttpResponse("pagamento")