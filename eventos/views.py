from django.shortcuts import render,  HttpResponse
from departamentos.models import Departamentos
from eventos.models import Eventos
from django.shortcuts import redirect
from eventos.forms import EventoForm

def todos(request):
    mensagens = ['temos' , 'outro qui','mais outro']
    mensagens.append('novo item agora')
    contexto = {
        'departamentos': Departamentos.objects.all(),
        'eventos' : Eventos.objects.all(),
        'form' : EventoForm,
        'mensagens' : mensagens,
        'error' : False,
        'sucesso': True,

    }
    return render(request, 'eventos/index.html', contexto)

def cadastrar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    return redirect('/eventos')