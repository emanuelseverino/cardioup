from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()


class Clinica(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='clinicas', blank=True, null=True)
    nome = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return '%s' % self.nome

    class Meta:
        ordering = ['nome', ]
