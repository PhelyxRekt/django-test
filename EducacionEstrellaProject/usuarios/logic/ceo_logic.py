
from comentarios.logic.comentarios_logic import get_comentarios
from citas.logic.citas_logic import get_citas


def get_estado_estudiante(var_cedula):
    citas = get_citas(var_cedula)
    comentarios =get_comentarios(var_cedula)
    return [citas, comentarios]