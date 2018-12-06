from django.shortcuts import render, HttpResponse


def inicio(request):
    return HttpResponse("turmas")
