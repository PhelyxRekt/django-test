from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('usuario/<int:cedula>', views.citas_view, name='citas_view'),
]