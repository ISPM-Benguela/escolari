from django import forms 
from cursos.models import Cursos

class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos 
        fields = ('nome', )