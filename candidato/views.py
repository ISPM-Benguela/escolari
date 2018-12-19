from django.shortcuts import render, HttpResponse
from candidato.models import Candidato
from departamentos.models import Departamentos
from candidato.forms import CandidatoForm
from candidato.models import Candidato
from mensagem.models import Mensagem

def inicio(request):
    return render(request, 'candidato/inicio.html', {
        'departamento': Departamentos.objects.all(),
        'form': CandidatoForm,
        'candidatos' : Candidato.objects.all(),

        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    })

def enviar_candidatura(request):

    form = CandidatoForm(request.POST or None)

    if request.method == 'POST':
        nome = request.POST.get('nome','')
        sobrenome = request.POST.get('sobrenome','')
        nobi = request.POST.get('nobi')
        candidatura = request.POST.get('candidatura','')


        if form.is_valid():
            form.save()

            return HttpResponse("candidatura enviada com sucesso!")
        else:
            return HttpResponse("Ocorreu um erro")


        return HttpResponse("%s %s %s %s" % (nome, sobrenome, nobi, candidatura))
    return render(request, 'candidato/inicio', {
        'departamento': Departamento.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
        
    })