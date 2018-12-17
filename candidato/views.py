from django.shortcuts import render, HttpResponse
from candidato.models import Candidato

def inicio(request):
    return HttpResponse("candidato")

def enviar_candidatura(request):

    if request.method == 'POST':
        nome = request.POST.get('nome','')
        sobrenome = request.POST.get('sobrenome','')
        nobi = request.POST.get('nobi')
        candidatura = request.POST.get('candidatura','')
        return HttpResponse("%s %s %s %s" % (nome, sobrenome, nobi, candidatura))
    return HttpResponse("candidatura")