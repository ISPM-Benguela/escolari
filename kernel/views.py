from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db.models import Q
from departamentos.models import Departamentos
from salas.models import Turmas
from usuarios.models import Perfil
from candidato.forms import CandidatoForm
from eventos.models import Eventos
from mensagem.models import Mensagem
from candidato.models import Candidato

def inicio(request):
   
    contaEstudante = Perfil.objects.filter(
        Q(tipo_perfil__startswith='E')
    ).count()

    contaFuncionario = Perfil.objects.filter(
        Q(tipo_perfil__startswith='F') |  Q(tipo_perfil__startswith='P')
    ).count()

    return render(request,'kernel/inicio.html',{

        'departNo' : Departamentos.objects.all().count(),
        'turmaNo' : Turmas.objects.all().count(),
        'estudanteNo' : contaEstudante,
        'funcionarioNo' : contaFuncionario,
        'form' : CandidatoForm,
        'eventos' : Eventos.objects.all(), 
        })

def sair(request):
    logout(request)

    return redirect('/')
    
    