from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from departamentos.models import Departamentos
from anolectivo.models import AnoLectivo
from django.shortcuts import get_object_or_404
from anolectivo.forms import AnolectivoForm
from candidato.models import Candidato
from mensagem.models import Mensagem


def inicio(request):
    contexto = {
        'departamentos' : Departamentos.objects.all(),
        'anolectivo' : AnoLectivo.objects.all(),
        'form' : AnolectivoForm,

        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    }
    if request.method == 'POST':
        return HttpResponse("bvindo do formulario")
    return render(request, 'ano/inicio.html', contexto)

def cadastrar_anolectivo(request):
    form = AnolectivoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    messages.success(request, 'Ano lectivo cadastrado com sucesso.')
    return HttpResponseRedirect('/painel/ano')

def editar_anolectivo(request, nome):
    instance = get_object_or_404(AnoLectivo, ano=nome)
    form = AnolectivoForm(request.POST or None, instance=instance)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Ano lectivo actualizado com sucesso.')
            return HttpResponseRedirect('/painel/ano')
    contexto = {
        "instance" : instance,
        "form" : form,
        "departamentos" : Departamentos.objects.all(),
    }
    
    return render(request, 'ano/editar.html', contexto )

def eliminar_anolectivo(request, nome):
    mensagens = []
    erro = False 
    sucesso = False 
    obj = AnoLectivo.objects.get(ano=nome)
    if obj:
        obj.delete()
        messages.warning(request, 'Ano lectivo eliminado com sucesso. ')
        return HttpResponseRedirect('/painel/ano')
    return HttpResponseRedirect('/ano')

def actualizar_anolectivo(request, nome):
    return HttpResponse("actualizar")