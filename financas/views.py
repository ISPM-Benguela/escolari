from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from departamentos.models import Departamentos
from cursos.models import Cursos
from candidato.models import Candidato
from mensagem.models import Mensagem
from cursos.forms import CursoForm
from django.contrib import messages
from financas.models import Pagamento
from financas.forms import PagamentoForm


def todos(request):
    return render(request, 'financas/index.html', {
        'departamentos' : Departamentos.objects.all(),
        'pagamentos': Pagamento.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
        'form' : PagamentoForm,
    })

def cradastrar_valor_propinas(request):
    form = PagamentoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Pagamento cadastrado com sucesso.')
            return HttpResponseRedirect('/painel/fanancas/')
    return HttpResponse("Error ao cadastrar pagamento")

def editar_valor_propinas(request, num):
    instance = get_object_or_404(Pagamento, id=num)
    form = PagamentoForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Pagamento actualizado com sucesso')
            return HttpResponseRedirect('/painel/fanancas/')

    contexto = {
        "instance" : instance,
        "form" : form,
        "departamentos" : Departamentos.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    }
    
    return render(request, 'financas/editar.html', contexto )


def eliminar_pagamento(request, num):
    pagamento = get_object_or_404(Pagamento, id=num)
    pagamento.delete()
    messages.warning(request, 'Pagamento eliminado com sucesso.')

    return HttpResponseRedirect("/painel/fanancas/")

