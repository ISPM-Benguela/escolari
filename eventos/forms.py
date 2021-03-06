from django import forms
from eventos.models import Eventos

class EventoForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ('titulo','imagem','local','data_inicio','data_termino',)