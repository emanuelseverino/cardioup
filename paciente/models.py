from clinica.models import Clinica
from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()


class Paciente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.clinica, self.nome)

    class Meta:
        ordering = ['-criado_em', ]
