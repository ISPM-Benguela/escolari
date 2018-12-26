from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from departamentos.models import Departamentos
from cursos.models import Cursos
from candidato.models import Candidato
from mensagem.models import Mensagem
from cursos.forms import CursoForm


def todos(request):
    return render(request, 'cursos/index.html', {
        'departamentos' : Departamentos.objects.all(),
        'cursos': Cursos.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
        'form' : CursoForm,
    })

def cadastrar_curso(request):
    return HttpResponseRedirect('acadad')
    
def editar_curso(request, id):
    instance = get_object_or_404(Cursos, id=id)
    form = CursoForm(request.POST or None, instance=instance)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cursos')
    contexto = {
        "instance" : instance,
        "form" : form,
        "departamentos" : Departamentos.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    }
    
    return render(request, 'cursos/editar.html', contexto )

def eliminar_curso(request, id):
    instance = get_object_or_404(Cursos, id=id)
    instance.delete()

    return HttpResponseRedirect('cursos')
    