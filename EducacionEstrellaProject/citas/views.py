from .logic import citas_logic as cl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def citas_view(request, cedula):
    if request.method == 'GET':
        citas_dto = cl.get_citas(cedula)
        citas = serializers.serialize('json', citas_dto)
        return HttpResponse(citas, 'application/json')