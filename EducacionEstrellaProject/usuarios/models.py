from django.db import models

class Usuario(models.Model):
    cedula = models.IntegerField(default=None)
    nombre = models.CharField(max_length=50)
    universidad = models.CharField(max_length=50, blank=True, null=True)
    ESTUDIANTE = 'ES'
    MENTOR = 'ME'
    CEO = 'CE'
    tipos = [
        (ESTUDIANTE, 'Estudiante'),
        (MENTOR, 'Mentor'),
        (CEO, 'CEO'),
    ]
    tipo = models.CharField(
        max_length=2,
        choices=tipos
    )

    def __str__(self):
        return '{}'.format(self.cedula)
