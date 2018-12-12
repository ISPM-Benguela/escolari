from django import forms
from meses.models import Meses

class MesesForm(forms.ModelForm):
    model = Meses
    fields = ('mes',) 