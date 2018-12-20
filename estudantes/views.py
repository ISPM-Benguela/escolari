import datetime
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from departamentos.models import Departamentos
from estudantes.forms import EstudanteForm
from usuarios.models import Perfil
from propinas.models import Propinas
from candidato.models import Candidato
from mensagem.models import Mensagem
from django.shortcuts import get_object_or_404
from usuarios.forms import EstudanteForm
from django.contrib.auth.models import User

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

def cadastrar_estudante(request):

    if request.method == 'POST':
        _nome = request.POST.get('nome')
        _senha = request.POST.get('senha')

        estudante = User(username=_nome)
        estudante.save()
        estudante.set_password(_senha)
        estudante.save()

        if estudante:
            instance = get_object_or_404(Perfil, user=estudante)
            form = EstudanteForm(request.POST or None, instance=instance)
        
        return render(request, 'estudantes/turma.html',{
            'form' : form,
            'instance': instance,
        })
def cadastrar_estudante_turma(request):
    form = EstudanteForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/estudantes')


def visualizar_estudante(request, num):
    estudante = get_object_or_404(User, id=num)

    contex
    return HttpResponse(num) 