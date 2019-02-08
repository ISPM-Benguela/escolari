from django import forms 
from financas.models import Pagamento

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento 
        fields = ('valor','tipo_servico', )