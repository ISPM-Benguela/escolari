from django.db import models
import datetime

class Candidato(models.Model):

    
    FUNCIONARIO = 'F'
    ESTUDANTE= 'E'

    CANDIDATURA = (
        (FUNCIONARIO, 'Funcionario'),
        (ESTUDANTE, 'Estudante'),
    )

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    noBI = models.CharField(max_length=100)
    candidatura = models.CharField( max_length=1, choices=CANDIDATURA, default=ESTUDANTE,  blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    novo = models.BooleanField(default=True)
    enviado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Candidatura"
        verbose_name_plural = "cadidaturas"
    
    def __str__(self):
        return self.nome