from ..models import Cita
def get_citas(var_cedula):
    citas = Cita.objects.filter(usuario__cedula = var_cedula)
    return citas