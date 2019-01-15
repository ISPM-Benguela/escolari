from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from departamentos.models import Departamentos
from salas.models import Turmas
from salas.forms import TurmaForm
from mensagem.models import Mensagem
from candidato.models import Candidato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.models import User
from estudantes.models import Estudantes
from usuarios.forms import EstudanteForm
from candidato.models import Candidato
from mensagem.models import Mensagem
from usuarios.models import Perfil
from django.db.models import Q
from django.contrib import messages

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
        'userform': UserCreationForm,
    })

def cadastrar_turma(request):

    senha = '1cristo2bom3'

    if request.method == 'POST':
        _nome = request.POST.get('nome')
        _sobrenome = request.POST.get('sobrenome')
        _turma = request.POST.get('turma')
        _email = request.POST.get('email')

        user = User(username=_nome)
        user.set_password(senha)
        user.save()

        if user:
            return HttpResponse(user.perfil.turma.get_turma)
    return HttpResponse("nao")
    

def visualizar_turma(request, num):
    turma = get_object_or_404(Turmas, id=num)
    estudantes = Estudantes.objects.filter(
        Q(turma=turma)
    )

    
    return render(request, 'turmas/turma.html',{
        'departamentos' : Departamentos.objects.all(),
        'form' : TurmaForm,
        'estudanteform' : EstudanteForm,
        'turma' : turma,
        'estudantes' : estudantes,
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    })
def cadastrar_estudante_turma(request):
    if request.method == 'POST':
        if not request.POST.get('nome') or not request.POST.get('turma'):
            messages.warning(request, 'O campo nome nao deve estar vazio.')
            return HttpResponseRedirect('/painel/turmas/visualizar/%s/' % request.POST.get('turma'))
        else:
            _nome = request.POST.get('nome')
            _senha = "password"
            _turma = request.POST.get('turma')

            turma = Turmas.objects.get(id=_turma)
            user = User.objects.create(username=_nome, password=_senha)
            perfil = Perfil.objects.get(id=user.id)
            perfil.tipo_perfil = 'E'
            perfil.save()

            estudante = Estudantes()
            estudante.peril = perfil
            estudante.turma = turma
            estudante.nome = user.username
            estudante.save()

            messages.success(request, 'Estudante cadastrado com sucesso.')
            return HttpResponseRedirect('/painel/turmas/visualizar/%s/' % request.POST.get('turma'))
    
    messages.warning(request, 'Ops! houve um erro tentar mais tarde')
    return HttpResponseRedirect('painel/turmas')
    