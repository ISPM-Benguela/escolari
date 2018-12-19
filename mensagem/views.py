from django.shortcuts import render, HttpResponse
from mensagem.models import Mensagem

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
            return HttpResponse("mensagrm enviada")
        else:
            return HttpResponse("nao enviada")



    return HttpResponse("nao guarda este dados nao e segura tira fora este usuario mau")
