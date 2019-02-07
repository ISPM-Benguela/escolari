

from django import forms 
from meses.models import Meses

class MesesForm(forms.ModelForm):
    class Meta:
        model = Meses 
        fields = ('mes', )