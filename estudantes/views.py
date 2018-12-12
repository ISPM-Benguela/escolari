from django.shortcuts import render
from django.db.models import Q
from departamentos.models import Departamentos
from estudantes.forms import EstudanteForm
from usuarios.models import Perfil

def inicio(request):
    queryset = Perfil.objects.filter(tipo_perfil='E')
    contexto = {
        'departamentos' : Departamentos.objects.all(),
        'form' : EstudanteForm,
        'estudantes': queryset,
    }
    return render(request, 'estudantes/inicio.html', contexto)