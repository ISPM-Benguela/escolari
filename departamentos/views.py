from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from departamentos.models import Departamentos
from departamentos.forms import DepartamentoForm
from candidato.models import Candidato
from mensagem.models import Mensagem
from django.contrib import messages

def todos(request):

    return render(request, 'departamentos/todos.html', {
        'funcionarios': User.objects.all(),
        'departamentos' : Departamentos.objects.all(),
        'form' : DepartamentoForm(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    })
def cradastrar_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento cadastrado com sucesso')
        return HttpResponseRedirect('/painel/departamentos/')
    return HttpResponse("NO OK")

def editar_departamento(request, nome):

    departamento = Departamentos.objects.get(nome=nome)
    funcionarios = departamento.funcionario.all()

    return render(request, 'departamentos/editar.html', {
        'departamento': departamento,
        'departamentos': Departamentos.objects.all(),
        'form' : DepartamentoForm(),
        'funcionarios' : departamento.funcionario.all(),
        'departamentos': Departamentos.objects.all(),
    })    

def actualizar_departamento(request, nome):
    instance = get_object_or_404(Departamentos, nome=nome)
    form = DepartamentoForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, 'Departamento actualizado com sucesso.')
        return HttpResponseRedirect('/painel/departamentos')

    contexto = {
        "nome": instance.nome,
        "instance" : instance,
        "form" : form,
        'departamentos': Departamentos.objects.all(),
    }
    return render(request, "departamentos/actualizar.html", contexto)

def eliminar_departamento(request, nome):
    instance = get_object_or_404(Departamentos, nome=nome)
    instance.delete()

    messages.warning(request, 'Departamento eliminado.')
    return HttpResponseRedirect('/painel/departamentos')

