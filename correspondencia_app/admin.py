from django.contrib import admin
from .models import CorrespondenciaEntrada, DocumentManager

@admin.register(DocumentManager)
class DocumentManagerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'asunto', 'gestor', 'estado', 'fecha_recepcion')
    list_filter = ('estado', 'gestor', 'fecha_recepcion')
    search_fields = ('numero_documento', 'asunto', 'remitente', 'destinatario')
