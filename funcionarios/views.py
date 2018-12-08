from django.shortcuts import render , HttpResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from  django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from departamentos.models import Departamentos
from funcionarios.forms import FuncionarioForm
from usuarios.models import Perfil



# Create your views here.
def todos(request):
    queryset = Perfil.objects.filter(
        Q(tipo_perfil__startswith='F')
    )
    return render(request, 'funcionarios/index.html', {
        'funcionarios' : queryset,
        'form' : UserCreationForm,
        'departamentos' : Departamentos.objects.all(),
    })
def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
    return redirect('/funcionarios')

def editar_funcionario(request, nome):
    instance = get_object_or_404(User, username=nome)
    form = UserCreationForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
    contexto = {
        "instance" : instance,
        "form" : form,
        "departamentos" : Departamentos.objects.all(),
    }
    
    return render(request, 'funcionarios/editar.html', contexto )

def actualizar_funcionario(request, nome):
    return HttpResponse("%s" . format(nome))