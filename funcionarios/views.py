from django.shortcuts import render , HttpResponse
from django.shortcuts import redirect
from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from departamentos.models import Departamentos
from funcionarios.forms import FuncionarioForm


# Create your views here.
def todos(request):
    return render(request, 'funcionarios/index.html', {
        'funcionarios' : User.objects.all(),
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
    funcionario = User.objects.get(username=nome)
    return render(request, 'funcionarios/editar.html', {
        'funcionario' : funcionario,
        'departamentos' : Departamentos.objects.all(),
    })