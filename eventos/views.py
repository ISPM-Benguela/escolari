from django.shortcuts import render,  HttpResponse
from django.shortcuts import get_object_or_404
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
        'sucesso': False,

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
        return redirect('/eventos')
    else:
        mensagens.append('Algo ocorreu mal')
        erro = True 
        return render(request, 'eventos/index.html',{
            'erro': erro,
            'mensagens': mensagens,
        })
def editar_eventos(request, num):
    obj = get_object_or_404(Eventos, num)
    mensagens = []
    erro = False 
    sucesso = False 

    if obj:
        sucesso = True 
        mensagens.append("Evento removido com sucesso!")
        obj.delete()
    return render(request, 'eventos/index.html',{
        'sucesso' : sucesso,
        'mensagens' : mensagens,
    })

def remover_eventos(request, num):
    
    mensagens = []
    erro = False 
    sucesso = False 
    obj = Eventos.objects.get(id=num)
    obj.delete()
        
    return render(request, 'eventos/index.html', {
        'sucesso' : True,
        'messagem': 'Evento Eliminado com sucesso',
        'form': EventoForm,
        'eventos' : Eventos.objects.all(),
    })

      
        

        
        

   # return redirect('/eventos')