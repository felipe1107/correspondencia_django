from django.contrib import admin
from .models import EntradaCorrespondencia, SalidaCorrespondencia, Gestor

@admin.register(EntradaCorrespondencia)
class EntradaCorrespondenciaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_recepcion', 'remitente', 'destinatario', 'departamento_destino', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')
    list_filter = ('fecha_recepcion', 'estado')

@admin.register(SalidaCorrespondencia)
class SalidaCorrespondenciaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_envio', 'remitente', 'destinatario', 'departamento_origen', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')
    list_filter = ('fecha_envio', 'estado')

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'fecha_ingreso')
    search_fields = ('nombre', 'correo')
    list_filter = ('fecha_ingreso',)
