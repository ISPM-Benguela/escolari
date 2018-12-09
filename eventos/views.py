from django.shortcuts import render,  HttpResponse
from departamentos.models import Departamentos
from eventos.models import Eventos
from django.shortcuts import redirect
from eventos.forms import EventoForm

def todos(request):
    contexto = {
        'departamentos': Departamentos.objects.all(),
        'eventos' : Eventos.objects.all(),
        'form' : EventoForm,
    }
    return render(request, 'eventos/index.html', contexto)

def cadastrar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    return redirect('/eventos')