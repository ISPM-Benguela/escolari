import datetime
from django.shortcuts import render
from django.db.models import Q
from departamentos.models import Departamentos
from estudantes.forms import EstudanteForm
from usuarios.models import Perfil
from propinas.models import Propinas
from candidato.models import Candidato
from mensagem.models import Mensagem

def inicio(request):
    queryset = Perfil.objects.filter(tipo_perfil='E')
    
    contexto = {
        'departamentos' : Departamentos.objects.all(),
        'form' : EstudanteForm,
        'estudantes': queryset,
        'date_actual' : datetime.date.today(),
        'ultima_propina' : Propinas.objects.last(),
        
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    }
    return render(request, 'estudantes/inicio.html', contexto)