from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from departamentos.models import Departamentos
from anolectivo.models import AnoLectivo
from django.shortcuts import get_object_or_404
from anolectivo.forms import AnolectivoForm

def inicio(request):
    contexto = {
        'departamentos' : Departamentos.objects.all(),
        'anolectivo' : AnoLectivo.objects.all(),
        'form' : AnolectivoForm,
    }
    if request.method == 'POST':
        return HttpResponse("bvindo do formulario")
    return render(request, 'ano/inicio.html', contexto)

def cadastrar_anolectivo(request):
    form = AnolectivoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/ano')

def editar_anolectivo(request, nome):
    return HttpResponse(nome)