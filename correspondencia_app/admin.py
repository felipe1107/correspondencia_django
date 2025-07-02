from django.contrib import admin
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_recepcion', 'remitente', 'destinatario', 'asunto', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')

@admin.register(CorrespondenciaSalida)
class CorrespondenciaSalidaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_envio', 'remitente', 'destinatario', 'asunto', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento')
    search_fields = ('nombre', 'departamento')
