from django import forms

from departamentos.models import Departamentos

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = ['nome', 'funcionario']
