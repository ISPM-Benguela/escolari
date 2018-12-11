from django import forms 
from estudantes.models import Estudantes

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudantes
        fields = ('peril','turma', 'nome',)