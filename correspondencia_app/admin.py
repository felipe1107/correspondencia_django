from django.contrib import admin
from .models import EntradaCorrespondencia, SalidaCorrespondencia, Gestor

@admin.register(EntradaCorrespondencia)
class EntradaCorrespondenciaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_recepcion', 'remitente', 'destinatario', 'departamento_destino', 'estado')

@admin.register(SalidaCorrespondencia)
class SalidaCorrespondenciaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_envio', 'remitente', 'destinatario', 'medio_envio')

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'departamento', 'correo', 'telefono')
