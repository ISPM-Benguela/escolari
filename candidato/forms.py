from django import forms
from candidato.models import Candidato

class CandidatoForm(forms.ModelForm):
   class Meta:
        model = Candidato
        fields = ('nome', 'sobrenome','noBI','candidatura',)
    