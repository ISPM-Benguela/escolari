from django.db import models



class Mensagem(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(13)
    assunto = models.CharField(255)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome 
    
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mengens"
