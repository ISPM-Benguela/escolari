from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from departamentos.models import Departamentos
from salas.models import Turmas
from salas.forms import TurmaForm
from mensagem.models import Mensagem
from candidato.models import Candidato
from django.contrib.auth.forms import UserCreationForm
from usuarios.forms import EstudanteForm
from candidato.models import Candidato
from mensagem.models import Mensagem

def todos(request):
    turmas = Turmas.objects.all()
    return render(request, 'turmas/index.html', {
        'departamentos': Departamentos.objects.all(),
        'turmas' : turmas,
        'form' : TurmaForm,
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    })

def cadastrar_turma(request):
    if request.method == 'POST':
        _nome = request.POST.get('nome')
        _sobrenome = request.POST.get('sobrenome')
        _nome = request.POST.get('nome')
        _nome = request.POST.get('nome')

        return HttpResponse("form")
    return HttpResponse("nao")
    

def visualizar_turma(request, turma):
    turma = get_object_or_404(Turmas, nome=turma)
    return render(request, 'turmas/turma.html',{
        'departamentos' : Departamentos.objects.all(),
        'form' : TurmaForm,
        'estudanteform' : EstudanteForm,
        'turma' : turma,
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    })