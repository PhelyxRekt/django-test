from email.policy import default
from django.db import models

from usuarios.models import Usuario

class Cita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    resultado = models.CharField(max_length=50)
    fecha = models.DateTimeField()


    def __str__(self):
        return '{}'.format(self.resultado)