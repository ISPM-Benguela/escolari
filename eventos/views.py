from django.shortcuts import render,  HttpResponse, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from departamentos.models import Departamentos
from eventos.models import Eventos
from django.shortcuts import redirect
from eventos.forms import EventoForm
from candidato.models import Candidato
from mensagem.models import Mensagem

def todos(request):
    mensagens = ['temos' , 'outro qui','mais outro']
    mensagens.append('novo item agora')
    contexto = {
        'departamentos': Departamentos.objects.all(),
        'eventos' : Eventos.objects.all(),
        'form' : EventoForm,
        'mensagens' : mensagens,
        'error' : False,
        'sucesso': False,
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),

    }
    return render(request, 'eventos/index.html', contexto)

def cadastrar_evento(request):
    mensagens = []
    erro = False 
    sucesso = False 

    if request.method == 'POST' and request.FILES['imagem']:
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento cadastrado com sucesso.')
        return redirect('/painel/eventos')
    else:
        messages.warning(request, 'Algo correu mal evento nao criado.')
        return redirect('/painel/eventos')

def editar_eventos(request, num):
    instance = Eventos.objects.get(id=num)

    if request.method == 'POST' and request.FILES:
        return HttpResponse("vem do form")

    form = EventoForm(request.POST or None, instance=instance)
    return render(request, 'eventos/editar.html', {
        'instance': instance,
        'messagem': 'Evento Eliminado com sucesso',
        'form': form,
        'eventos' : Eventos.objects.all(),
    })

def remover_eventos(request, num):
    
    mensagens = []
    erro = False 
    sucesso = False 
    obj = Eventos.objects.get(id=num)
    obj.delete()
    messages.warning(request, 'Evento eliminado com sucesso.')
    return redirect('/painel/eventos')

def actualizar_eventos(request, num):
    return HttpResponse("actualizar evtnto")
        

        
        

   # return redirect('/eventos')