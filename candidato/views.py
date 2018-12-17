from django.shortcuts import render, HttpResponse


def inicio(request):
    return HttpResponse("candidato")

def enviar_candidatura(request):
    return HttpResponse("candidatura")