from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.models import User
from django.db.models import Q
from departamentos.models import Departamentos
from salas.models import Turmas
from usuarios.models import Perfil
from candidato.forms import CandidatoForm
from eventos.models import Eventos
from mensagem.models import Mensagem

def inicio(request):
    queryset = Perfil.objects.filter(
        Q(tipo_perfil__startswith='E')
    )
    contaEstudante = Perfil.objects.filter(
        Q(tipo_perfil__startswith='E')
    ).count()

    contaFuncionario = Perfil.objects.filter(
        Q(tipo_perfil__startswith='F')
    ).count()

    
    if request.user.is_authenticated():
        return render(request, 'painel/index.html', {

        'departamentos': Departamentos.objects.all(),
        'departNo' : Departamentos.objects.all().count(),
        'turmaNo' : Turmas.objects.all().count(),
        'estudanteNo' : contaEstudante,
        'funcionarioNo' : contaFuncionario,
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        })
    return render(request,'kernel/inicio.html',{

        'departNo' : Departamentos.objects.all().count(),
        'turmaNo' : Turmas.objects.all().count(),
        'estudanteNo' : contaEstudante,
        'funcionarioNo' : contaFuncionario,
        'form' : CandidatoForm,
        'eventos' : Eventos.objects.all(), 
        })
    