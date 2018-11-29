from django.shortcuts import render
from departamentos.models import Departamentos

def todos(request):
    return render(request, 'turmas/index.html', {
        'departamentos': Departamentos.objects.all(),
    })