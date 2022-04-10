from ..models import Comentario
def get_comentarios(var_cedula):
    comentarios = Comentario.objects.filter(usuario__cedula = var_cedula)
    return comentarios