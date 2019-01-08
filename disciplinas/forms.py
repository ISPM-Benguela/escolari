from django import forms
from disciplinas.models import Disciplina

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ('nome','cursos',)