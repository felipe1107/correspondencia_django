# correspondencia_app/admin.py
from django.contrib import admin
from .models import Departamento, Gestor, CorrespondenciaEntrada, CorrespondenciaSalida

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo')

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'remitente', 'destinatario', 'fecha_recepcion', 'estado')

@admin.register(CorrespondenciaSalida)
class CorrespondenciaSalidaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'destinatario', 'fecha_envio', 'estado')
