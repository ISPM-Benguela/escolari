from django.db import models



class Mensagem(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=13)
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()
    por_ler = models.BooleanField(default=True)

    def __str__(self):
        return self.nome 
    
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mengens"
