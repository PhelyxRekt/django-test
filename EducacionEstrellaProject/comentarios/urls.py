from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('usuario/<int:cedula>', views.comentarios_view, name='comentarios_view'),
]