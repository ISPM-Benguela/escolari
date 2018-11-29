from django.shortcuts import render
from  django.contrib.auth.models import User
from departamentos.models import Departamentos

def todos(request):
    return render(request, 'turmas/index.html',{
        'departamentos': Departamentos.objects.all()
    })
