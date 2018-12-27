from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required


def inicio(request):
    contaEstudante = Perfil.objects.filter(
        Q(tipo_perfil__startswith='E')
    ).count()

    contaFuncionario = Perfil.objects.filter(
        Q(tipo_perfil__startswith='F') |  Q(tipo_perfil__startswith='P')
    ).count()

    """
    if request.user.is_authenticated():
        return render(request, 'painel/index.html', {

        'departamentos': Departamentos.objects.all(),
        'departNo' : Departamentos.objects.all().count(),
        'turmaNo' : Turmas.objects.all().count(),
        'estudanteNo' : contaEstudante,
        'funcionarioNo' : contaFuncionario,
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
        })"""

    if request.user.is_authenticated():
        
        return HttpResponse("esta logado")
    else:
        return redirect('/')
