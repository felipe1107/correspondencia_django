from django.contrib import admin
from .models import EntradaCorrespondencia, SalidaCorrespondencia, Gestor

@admin.register(EntradaCorrespondencia)
class EntradaCorrespondenciaAdmin(admin.ModelAdmin):
    list_display = (
        'numero_documento',
        'fecha_recepcion',
        'remitente',
        'destinatario',
        'departamento_destino',
        'estado',
    )
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')
    list_filter = ('estado', 'fecha_recepcion')

@admin.register(SalidaCorrespondencia)
class SalidaCorrespondenciaAdmin(admin.ModelAdmin):
    list_display = (
        'numero_documento',
        'fecha_envio',
        'remitente',
        'destinatario',
        'medio_envio',
    )
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')
    list_filter = ('medio_envio', 'fecha_envio')

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'cargo',
        'departamento',
        'correo',
        'telefono',
    )
    search_fields = ('nombre', 'cargo', 'departamento')
    list_filter = ('departamento',)
