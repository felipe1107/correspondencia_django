from django.contrib import admin
from .models import Gestor, CorrespondenciaEntrada, CorrespondenciaSalida

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')
    search_fields = ('nombre', 'correo')

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'asunto', 'gestor', 'fecha_recepcion')
    list_filter = ('fecha_recepcion',)
    search_fields = ('numero_documento', 'asunto', 'gestor__nombre')

@admin.register(CorrespondenciaSalida)
class CorrespondenciaSalidaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'asunto', 'fecha_envio', 'remitente', 'destinatario', 'estado')
    list_filter = ('fecha_envio', 'estado')
    search_fields = ('numero_documento', 'asunto', 'remitente', 'destinatario')
