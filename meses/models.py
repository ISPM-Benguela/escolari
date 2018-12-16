from django.db import models
import datetime

class Meses(models.Model):
    mes = models.CharField(max_length=255)
    criado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('mes',)
        verbose_name = "Mes"
        verbose_name_plural = "Meses"
        ordering = ['criado']

    def __str__(self):
        return self.mes
    
    def get_mes(self):
        return self.mes
