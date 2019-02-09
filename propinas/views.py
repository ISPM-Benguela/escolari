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
from financas.models import Pagamento
import  decimal
from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

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
    pagamento = get_object_or_404(Pagamento, tipo_servico='P')
    
    if request.method == 'POST':
        _prestacao = request.POST['prestacao']
        _mes = request.POST['mes']
        _ano = request.POST['ano']
        

        if _prestacao < "0":
            messages.warning(request, "Numero de Prestação não pode ser um número negativo.")
            return HttpResponseRedirect('/painel/propinas/pagar/%s/' % estudante.id)
        
        apagar = pagamento.valor * decimal.Decimal(_prestacao)

        return render(request, "propinas/confirmar.html", {
        'form' : PropinasForm(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
        'estudante': estudante,
        'ano' : AnoLectivo.objects.get(id=_ano),
        'mes' : Meses.objects.get(id=_mes),
        'apagar' : apagar,
        'prestacao' : _prestacao,
        
    })
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
        _mes = request.POST['mes']
        _apagar = request.POST['apagar']
        _estudante = request.POST['estudante']
        _prestacao = request.POST['prestacao']
        _ano = request.POST['ano']

    return HttpResponse("Nao vem do post")

