import datetime
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from departamentos.models import Departamentos
from estudantes.forms import EstudanteForm
from usuarios.models import Perfil
from propinas.models import Propinas
from candidato.models import Candidato
from mensagem.models import Mensagem
from django.shortcuts import get_object_or_404
from usuarios.forms import EstudanteForm
from django.contrib.auth.models import User
from  usuarios.models import Perfil
from salas.models import Turmas
from estudantes.models import Estudantes
from disciplinas.models import Disciplina

def inicio(request):
    queryset = Perfil.objects.filter(tipo_perfil='E')
    
    contexto = {
        'departamentos' : Departamentos.objects.all(),
        'form' : EstudanteForm,
        'estudantes': Estudantes.objects.all(),
        'date_actual' : datetime.date.today(),
        'ultima_propina' : Propinas.objects.last(),
        'turmas' : Turmas.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    }
    return render(request, 'estudantes/inicio.html', contexto)

def cadastrar_estudante(request):

    if request.method == 'POST':
        if not request.POST.get('nome') or not request.POST.get('senha') or not request.POST.get('turma'):
            messages.warning(request, 'Os Campos nao podem estar vazio')
            return HttpResponseRedirect('/painel/estudantes')
        else:
            _nome = request.POST.get('nome')
            _senha = request.POST.get('senha')
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

            
            return HttpResponseRedirect('/painel/estudantes')

    return HttpResponse('algo')

def cadastrar_estudante_turma(request):
    form = EstudanteForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/estudantes')


def visualizar_estudante(request, num):
    estudante = get_object_or_404(Estudantes, id=num)
    queryset = Disciplina.objects.filter(curso=estudante.turma.curso)
    

    return render(request, 'estudantes/cada.html', {
        'disciplinas' : queryset,
    })
