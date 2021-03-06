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
    turma = TurmaForm(request.POST)

    if request.method == 'POST':
        if turma.is_valid():
            messages.success(request, 'Turma cadastrado com sucesso.')
            turma.save()
        else:
            messages.success(request, 'Formulario vaio')
        return HttpResponseRedirect('/painel/turmas')
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

def editar_turma(request, num=None):
    turma = get_object_or_404(Turmas, id=num)
    form = TurmaForm(request.POST or None, instance=turma)

    estudantes = Estudantes.objects.filter(
        Q(turma=turma)
    )

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Turma actualizado com sucesso.')
            return HttpResponseRedirect('/painel/turmas')
    
    return render(request, 'turmas/editar.html',{
        'departamentos' : Departamentos.objects.all(),
        'form' : form,
        'turma': turma,
        'estudantes' : estudantes,
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    })

def eliminar_turma(request, num):
    turma = get_object_or_404(Turmas, id=num)
    turma.delete()

    messages.success(request, 'Turma eliminado com sucesso.')
    return HttpResponseRedirect('/painel/turmas')

def cadastrar_estudante_turma(request):
    if request.method == 'POST':
        if not request.POST.get('nome') or not request.POST.get('turma'):
            messages.warning(request, 'O campo nome nao deve estar vazio.')
            return HttpResponseRedirect('/painel/turmas/visualizar/%s/' % request.POST.get('turma'))
        else:
            _nome = request.POST.get('nome')
            _senha = "senha"
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
    