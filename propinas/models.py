from django.db import models
from django.contrib.auth.models import User
from meses.models import Meses
from anolectivo.models import AnoLectivo

class Propinas(models.Model):
    estundante = models.ForeignKey(User)
    mes = models.ManyToManyField(Meses, default="", blank=True)
    ano = models.ForeignKey(AnoLectivo)
    propina = models.IntegerField(default=0)
    total_propinas = models.IntegerField(default=0)
   # propina = models.DecimalField(decimal_places=2, default=0)

    def __str__(self):
        return "%s" % self.mes
    
    class Meta:
        verbose_name = "Pronina"
        verbose_name_plural = "Propinas"
        get_latest_by = 'mes'