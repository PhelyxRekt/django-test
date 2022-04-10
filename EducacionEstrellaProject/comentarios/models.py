from django.db import models

from usuarios.models import Usuario

class Comentario(models.Model):
    texto = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return '{}'.format(self.texto)
