from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from departamentos.models import Departamentos
from meses.models import Meses
from candidato.models import Candidato
from mensagem.models import Mensagem
from meses.forms import MesesForm
from django.contrib import messages


def todos(request):
    return render(request, 'meses/index.html', {
        'departamentos' : Departamentos.objects.all(),
        'meses': Meses.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
        'form' : MesesForm,
    })

def cadastrar_mes(request):
    if request.method == 'POST':
        form = MesesForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Mes cadastrado com sucesso.')    
        return HttpResponseRedirect('/painel/meses')
    return HttpResponse('acadad')

def editar_mes(request):
    pass
def eliminar_mes(request):
    pass
