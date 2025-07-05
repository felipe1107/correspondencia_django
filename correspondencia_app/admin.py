from django.contrib import admin
from .models import Entrada, Salida, Gestor, Usuario

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_recepcion', 'remitente', 'destinatario', 'departamento_destino', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')


@admin.register(Salida)
class SalidaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_envio', 'remitente', 'destinatario', 'departamento_origen', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')


@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'correo', 'telefono')
    search_fields = ('nombre', 'cargo')


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'departamento')
    search_fields = ('user__username', 'departamento')
