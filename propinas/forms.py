from django import forms 
from propinas.models import Propinas

class PropinasForm(forms.ModelForm):
    class Meta:
        model = Propinas
        fields = ('mes', 'ano','propina',)