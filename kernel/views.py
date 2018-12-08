from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.models import User
from departamentos.models import Departamentos
from salas.models import Turmas

def inicio(request):
    if request.user.is_authenticated():
        return render(request, 'painel/index.html', {

        'departamentos': Departamentos.objects.all(),
        'departNo' : Departamentos.objects.all().count(),
        'turmaNo' : Turmas.objects.all().count(),
        })
    return render(request,'kernel/inicio.html')