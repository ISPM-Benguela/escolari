from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    if request.user.is_authenticated():
        return HttpResponse("esta logado")
    else:
        return HttpResponse("Nao esta logado")
