from django.shortcuts import render
from django.contrib.auth.models import User
from departamentos.models import Departamentos
from departamentos.forms import DepartamentoForm


def todos(request):

    return render(request, 'departamentos/todos.html', {
        'funcionarios': User.objects.all(),
        'departamentos': Departamentos.objects.all(),
    })
def cradastrar_departamento(request):
    if request.method == 'POST':
        forms = DepartamentoForm(request.POST)
        if forms.is_valid():
             #return HttpResponse(forms.cleaned_data['nome'])
             forms.save()
             return redirect('departamentos')
        return HttpResponse("virou opps")

def editar_departamento(request, nome):

    departamento = Departamentos.objects.get(nome=nome)
    funcionarios = departamento.funcionario.all()

    return render(request, 'departamentos/editar.html', {
        'departamento': departamento,
        'departamentos': Departamentos.objects.all(),
        'forms' : DepartamentoForm(),
        'funcionarios' : departasmento.funcionario.all(),
    })    

def actualizar_departamento(request, nome):
    instance = get_object_or_404(Departamentos, nome=nome)
    form = DepartamentoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("nome"))
        instance.save()

    contexto = {
        "nome": instance.nome,
        "instance" : instance,
        "form" : form,
    }
    return render(request, "departamentos/actualizar.html", contexto)