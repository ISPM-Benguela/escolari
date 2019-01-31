from django import forms 
from propinas.models import Propinas

class PropinasForm(forms.ModelForm):
    class Meta:
        model = Propinas
        fields = ('estundante','mes', 'ano','propina','total_propinas',)