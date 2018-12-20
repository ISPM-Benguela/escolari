from django.shortcuts import render , HttpResponse, redirect
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from  django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from departamentos.models import Departamentos
from funcionarios.forms import FuncionarioForm
from usuarios.models import Perfil
from usuarios.forms import FunciornarioForm
from mensagem.models import Mensagem
from candidato.models import Candidato


# Create your views here.
def todos(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/funcionarios')
    
    return render(request, 'funcionarios/index.html', {
        'funcionarios' : Perfil.objects.filter(
            Q(tipo_perfil__startswith='F') |  Q(tipo_perfil__startswith='P')
        ),
        'form' : UserCreationForm,
        'departamentos' : Departamentos.objects.all(),
        'feed': Mensagem.objects.filter(por_ler=True).count(),
        'mensagens': Mensagem.objects.filter(por_ler=True),
        'feedcandidato': Candidato.objects.filter(novo=True).count(),
        'candidatos': Candidato.objects.filter(novo=True),
    })
def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            
    return redirect('/funcionarios')

def editar_funcionario(request, num):
    instance = get_object_or_404(User, id=num)
    perfil = get_object_or_404(Perfil, user=instance)

    form = UserCreationForm(request.POST or None, instance=instance)
    funcform = FuncionarioForm(request.POST or None, instance=perfil)

    if funcform.is_valid():
        funcform.save()

    contexto = {
        "instance" : instance,
        #"form" : form,
        'funcform' : funcform, 
        "departamentos" : Departamentos.objects.all(),
    }
    
    return render(request, 'funcionarios/editar.html', contexto )

def actualizar_funcionario(request, nome):
    return HttpResponse("%s" . format(nome))

def eliminar_funcionario(request, num):
    usuario = get_object_or_404(User, id=num)
    usuario.delete()

    return redirect('funcionarios')
    