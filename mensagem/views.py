from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib import messages
from mensagem.models import Mensagem
from departamentos.models import Departamentos
from candidato.models import Candidato

def inicio(request):
    

    if request.method == 'POST':
        _nome = request.POST.get('nome','')
        _email = request.POST.get('email','')
        _telefone = request.POST.get('telefone','')
        _assunto = request.POST.get('assunto','')
        _mensagem = request.POST.get('mensagem')

        confirmar = Mensagem(
            nome=_nome,
            email=_email,
            telefone=_telefone,
            assunto = _assunto,
            mensagem=_mensagem
        )
        confirmar.save()

        if confirmar:
            messages.success(request, 'Mensagem enviada com sucesso aguarda a respota.')
            return redirect('inicio')
        else:
            messages.warning(request, 'Algo corrreu mal, mensagem nao enviada.')
            return render('inicio')



    return render(request, 'mensagem/index.html', {
        'departamentos' : Departamentos.objects.all(),
        
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    })

def marcar_lido(request, num):
    mensagem = Mensagem.objects.get(id=num)
    mensagem.por_ler = False
    mensagem.save()

    messages.success(request, 'Messagem marcada como lida')

    return redirect('/painel/mensagem')

def todas_mensagens(request):
    return render(request, 'mensagem/todas.html', {
        'departamentos' : Departamentos.objects.all(),
        
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.all(),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    })

def eliminar_mensagem(request, num):
    mensagem = Mensagem.objects.get(id=num)
    mensagem.delete()

    messages.warning(request, 'Mensagem eliminada com sucesso.')

    return redirect('/painel/mensagem/todas/')

