from django import forms 
from estudantes.models import Estudantes

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudantes
        fields = ('turma','primeiro_nome','sobre_nome', 'nome','nome_encarregado','disciplinas',)