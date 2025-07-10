from django.contrib import admin
from .models import EntradaCorrespondencia, SalidaCorrespondencia, Gestor

@admin.register(EntradaCorrespondencia)
class EntradaCorrespondenciaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_recepcion', 'remitente', 'destinatario', 'asunto', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')

@admin.register(SalidaCorrespondencia)
class SalidaCorrespondenciaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_envio', 'remitente', 'destinatario', 'asunto', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'departamento')
    search_fields = ('nombre', 'correo', 'departamento')
