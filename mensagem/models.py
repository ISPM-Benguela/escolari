from django.db import models
import datetime


class Mensagem(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=13)
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()
    por_ler = models.BooleanField(default=True)
    enviado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome 
    
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mengens"
