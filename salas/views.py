from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from departamentos.models import Departamentos
from salas.models import Turmas
from salas.forms import TurmaForm

def todos(request):
    turmas = Turmas.objects.all()
    return render(request, 'turmas/index.html', {
        'departamentos': Departamentos.objects.all(),
        'turmas' : turmas,
        'form' : TurmaForm,
    })

def cadastrar_turma(request):
    form = TurmaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("nao e validao")
    return HttpResponseRedirect("/turmas")