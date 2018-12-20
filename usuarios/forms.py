from django import forms
from usuarios.models import Perfil


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('turma', 'disciplina','foto',)

class FunciornarioForm(forms.ModelForm):
    class Meta:
        model = Perfil 
        fields = ('tipo_perfil','foto','departamento',)