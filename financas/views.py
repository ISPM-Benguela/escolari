from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from departamentos.models import Departamentos
from cursos.models import Cursos
from candidato.models import Candidato
from mensagem.models import Mensagem
from cursos.forms import CursoForm
from django.contrib import messages


def todos(request):
    return render(request, 'financas/index.html', {
        'departamentos' : Departamentos.objects.all(),
        'cursos': Cursos.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
        'form' : CursoForm,
    })
