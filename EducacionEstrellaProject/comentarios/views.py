from .logic import comentarios_logic as cl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def comentarios_view(request, cedula):
    if request.method == 'GET':
        comentarios_dto = cl.get_comentarios(cedula)
        comentarios = serializers.serialize('json', comentarios_dto)
        return HttpResponse(comentarios, 'application/json')