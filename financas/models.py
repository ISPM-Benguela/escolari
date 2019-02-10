from django.db import models
from django.contrib.auth.models import User
class Pagamento(models.Model):

    PROPINA = 'P'
    MATRICULA = 'M'
    

    SERVICO = (

        (PROPINA, 'Propina'),
        (MATRICULA, 'Matricula')
    )

   
    valor = models.DecimalField("Total do valor",decimal_places=2, max_digits=100)
    tipo_servico = models.CharField('Tipo de serviço', max_length=1, choices=SERVICO, default=MATRICULA,  blank=True, null=True)
    prestacao = models.PositiveIntegerField(default=0)
    data = models.DateTimeField("Data do pagamento", auto_now_add=True)

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __str__(self):
        return self.valor
    
    def get_propina(self):
        return "%s" % self.valor