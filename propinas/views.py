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

    if request.method == 'POST':
        aluno = request.POST.get('estudante')
        ano = request.POST.get('ano')
        mes = request.POST.get('mes')
        propina = request.POST.get('propina')

        return HttpResponse("estudante: %s, anolectivo: %s, mes: %s, propina: %s" % (aluno, ano, mes, propina))
    return HttpResponse("pagamento")