from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from departamentos.models import Departamentos
from disciplinas.forms import DisciplinaForm, Disciplina
from cursos.models import Cursos

def inicio(request):
    return  render(request, 'disciplinas/inicio.html', {
        'departamentos' : Departamentos.objects.all(),
        'cursos' : Cursos.objects.all(),
        'form' : DisciplinaForm,
        'disciplinas' : Disciplina.objects.all(),
    })
def cadastrar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Algo foi mal')
            form.save()
            return HttpResponseRedirect('/painel/disciplina')
    return HttpResponseRedirect('/painel/disciplina')