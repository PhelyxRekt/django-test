from .logic import ceo_logic as cl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def estado_estudiante_view(request, cedula):
    if request.method == 'GET':
        estado_estudiante_dto = cl.get_estado_estudiante(cedula)
        citas = serializers.serialize('json', estado_estudiante_dto[0])
        comentarios = serializers.serialize('json', estado_estudiante_dto[1])
        return HttpResponse([citas, comentarios], 'application/json')