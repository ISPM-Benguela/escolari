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
    instance = get_object_or_404(AnoLectivo, ano=nome)
    form = AnolectivoForm(request.POST or None, instance=instance)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ano')
    contexto = {
        "instance" : instance,
        "form" : form,
        "departamentos" : Departamentos.objects.all(),
    }
    
    return render(request, 'ano/editar.html', contexto )

def eliminar_anolectivo(request, nome):
    mensagens = []
    erro = False 
    sucesso = False 
    obj = AnoLectivo.objects.get(ano=nome)
    if obj:
        obj.delete()
        return HttpResponseRedirect('/ano')
    return HttpResponseRedirect('/ano')

def actualizar_anolectivo(request, nome):
    return HttpResponse("actualizar")