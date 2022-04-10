


from usuarios.models import Usuario
from citas.models import Cita
from comentarios.models import Comentario

for i in range(0, 1501):
    Cita.objects.bulk_create([Cita(resultado="Cita "+str(i), fecha = "2022-04-01T16:19:56Z", usuario_id=1)])

for i in range(0, 1501):
    Comentario.objects.bulk_create([Comentario(texto = str(i), usuario_id=1)])


for i in range(0, 1501):
    Usuario.objects.bulk_create([Usuario(cedula = i, nombre = str(i), tipo = 'CE')])

