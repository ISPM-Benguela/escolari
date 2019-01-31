from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from departamentos.models import Departamentos
from  nivel.models import Nivel
from candidato.models import Candidato
from mensagem.models import Mensagem
from nivel.forms import NivelForm
from django.contrib import messages


def todos(request):
    return render(request, 'nivel/index.html', {
        'departamentos' : Departamentos.objects.all(),
        'nivel': Nivel.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
        'form' : NivelForm,
    })

def cadastrar_nivel(request):
    if request.method == 'POST':
        form = NivelForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Nivel academico cadastrado com sucesso')
        return HttpResponseRedirect('/painel/nivel')
    return HttpResponse('cadastrar nivel')

def editar_nivel(request, id):
    instance = get_object_or_404(Nivel, id=id)
    form = NivelForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Nivel academico actualizado com sucesso')
            return HttpResponseRedirect('/painel/nivel')

    contexto = {
        "instance" : instance,
        "form" : form,
        "departamentos" : Departamentos.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    }
    
    return render(request, 'nivel/editar.html', contexto )

def eliminar_nivel(request, id):
    instance = get_object_or_404(Nivel, id=id)
    instance.delete()
    messages.warning(request, 'Nivel academico eliminado com sucesso')
    return HttpResponseRedirect('/painel/nivel')
