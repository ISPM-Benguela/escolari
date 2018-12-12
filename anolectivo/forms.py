from django import forms 
from anolectivo.models import AnoLectivo

class AnolectivoForm(forms.ModelForm):
    class Meta:
        model = AnoLectivo
        fields = ("ano",)