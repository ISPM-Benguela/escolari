from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from departamentos.models import Departamentos
from disciplinas.models import Disciplina
from salas.models import Turmas
from propinas.models import Propinas

class Perfil(models.Model):

    ADMIN = 'A'
    FUNCIONARIO = 'F'
    ESTUDANTE= 'E'
    PROFESSOR = 'P'

    PERFIL = (
        (ADMIN, _('Administrador')),
        (FUNCIONARIO, _('Funcionario')),
        (ESTUDANTE, _('Estudante')),
        (PROFESSOR, _('Professor'))
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    departamento = models.ForeignKey(Departamentos, blank=True, null=True)
    primeiro_nome = models.CharField(_('Primeiro nome'), max_length=250, blank=True, null=True, default="")
    segundo_nome = models.CharField(_('Segundo nome'), max_length=250, blank=True, null=True, default="")
    tipo_perfil = models.CharField(_('Tipo de perfil'), max_length=1, choices=PERFIL, default=FUNCIONARIO,  blank=True, null=True)
    morada  = models.CharField(_('nome da turma'), max_length=250, blank=True, null=True, default="")
    foto = models.FileField(default='perfil/default.jpg', upload_to='perfil/', blank=True, null=True)
    # perfil do estudante

    turma = models.ForeignKey(Turmas, blank=True,  null=True)
    propinas = models.ManyToManyField(Propinas, blank=True)

    def __str__(self):
        return self.user.username
   

    @receiver(post_save, sender=User)
    def create_user_perfil(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_perfil(sender, instance, **kwargs):
        instance.perfil.save()

    def get_propina(self, id):
       # return Propinas.objects.latest()
        return Propinas.objects.all()
    
    def get_full_name(self):
        return "%s %s" % (self.primeiro_nome, self.segundo_nome)
       