import datetime
from django.shortcuts import render
from django.db.models import Q
from departamentos.models import Departamentos
from estudantes.forms import EstudanteForm
from usuarios.models import Perfil
from propinas.models import Propinas

def inicio(request):
    queryset = Perfil.objects.filter(tipo_perfil='E')
    
    contexto = {
        'departamentos' : Departamentos.objects.all(),
        'form' : EstudanteForm,
        'estudantes': queryset,
        'date_actual' : datetime.date.today(),
        'ultima_propina' : Propinas.objects.last(),
    }
    return render(request, 'estudantes/inicio.html', contexto)