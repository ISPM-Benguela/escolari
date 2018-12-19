from django import forms
from usuarios.models import Perfil


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('turma', 'disciplina','foto',)