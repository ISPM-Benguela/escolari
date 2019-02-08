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
from anolectivo.models import AnoLectivo
from candidato.models import Candidato
from mensagem.models import Mensagem
from anolectivo.models import AnoLectivo


@login_required
def inicio(request):
    return render(request, 'propinas/inicio.html',{
        'departamentos' : Departamentos.objects.all(),
        'estudantes' : Estudantes.objects.all(),
        'form' : PropinasForm(),
    })

@login_required
def pagar_propinas(request, num):
    
    estudante = get_object_or_404(Estudantes, id=num)
    if request.method == 'POST':
        return HttpResponse("vem do formulrios")
    return render(request, 'propinas/pagamentos.html', {
        'form' : PropinasForm(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
        'estudante': estudante,
        'ano' : AnoLectivo.objects.all(),
        'mes' : Meses.objects.all(),
        
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

