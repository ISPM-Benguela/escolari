from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from departamentos.models import Departamentos
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from meses.models import Meses
from anolectivo.models import AnoLectivo
from propinas.models import Propinas
import datetime


@login_required
def inicio(request):
    return render(request, 'propinas/inicio.html',{
        'departamentos' : Departamentos.objects.all(),
    })

@login_required
def pagar_propinas(request, nome):

    estudante = get_object_or_404(User, username=nome)

    return render(request, 'propinas/pagamentos.html',{
        'departamentos' : Departamentos.objects.all(),
        'estudante' : estudante,
        'meses': Meses.objects.all(),
        'anolectivos': AnoLectivo.objects.all(),
        'propinas' : Propinas.objects.all(),
        'mes_actual' : datetime.date.today(),
    })

@login_required
def cadastrar_pagamento(request):
    pagamento = None

    if request.method == 'POST':
        aluno = request.POST.get('estudante')
        ano = request.POST.get('ano')
        mes = request.POST.get('mes')
        propina = request.POST.get('propina')
        
        # Instancias
        _aluno = get_object_or_404(User, username=aluno)
        _mes = get_object_or_404(Meses, id=mes)
        _ano = get_object_or_404(AnoLectivo, id=ano)

        if not Propinas.objects.filter(mes=_mes).exists():
            pagamento = Propinas.objects.create(
                estundante=_aluno,
                mes=_mes,
                ano=_ano,
                propina=propina

             )
        else:
            return HttpResponse("mes ja existe")

        if pagamento:
            return HttpResponse("pago")
        else:
            return HttpResponse("nao pago")
        #return HttpResponse("estudante: %s, anolectivo: %s, mes: %s, propina: %s" % (aluno, ano, mes, propina))
    return HttpResponse("pagamento")

