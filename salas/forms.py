from django import forms
from salas.models import Turmas

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turmas
        fields = ('nome','numero_sala', 'ano','curso','nivel','periodo','responsavel',)