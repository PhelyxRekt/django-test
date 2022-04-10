from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('usuario/<int:cedula>', views.estado_estudiante_view, name='estado_estudiante_view'),
]