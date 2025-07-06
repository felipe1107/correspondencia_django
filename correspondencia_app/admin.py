from django.contrib import admin
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor, Usuario

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_recepcion', 'remitente', 'destinatario', 'asunto', 'departamento_destino', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')
    list_filter = ('estado', 'departamento_destino')

@admin.register(CorrespondenciaSalida)
class CorrespondenciaSalidaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_envio', 'remitente', 'destinatario', 'asunto', 'departamento_origen', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')
    list_filter = ('estado', 'departamento_origen')

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')
    search_fields = ('nombre', 'correo')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
