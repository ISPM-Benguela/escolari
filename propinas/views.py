from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from departamentos.models import Departamentos
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from meses.models import Meses
from anolectivo.models import AnoLectivo
from propinas.models import Propinas
from estudantes.models import Estudantes
from propinas.forms import PropinasForm
import datetime


@login_required
def inicio(request):
    return render(request, 'propinas/inicio.html',{
        'departamentos' : Departamentos.objects.all(),
        'estudantes' : Estudantes.objects.all(),
    })

@login_required
def pagar_propinas(request, num):

    estudante = get_object_or_404(Estudantes, id=num)

    return render(request, 'propinas/pagamentos.html',{
        'departamentos' : Departamentos.objects.all(),
        'form': PropinasForm(),
        'estudante' : estudante,
        'meses': Meses.objects.all(),
        'anolectivos': AnoLectivo.objects.all(),
        'propinas' : Propinas.objects.all(),
        'mes_actual' : datetime.date.today(),
    })

@login_required
def cadastrar_pagamento(request):

    form = PropinasForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Propina registado com sucesso.')
            return HttpResponseRedirect('painel/propinas')
    return HttpResponse("Nao vem do post")

