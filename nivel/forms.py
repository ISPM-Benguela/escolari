from django import forms 
from nivel.models import Nivel

class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel 
        fields = ('nome', )