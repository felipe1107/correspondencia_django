from django.contrib import admin
from .models import CorrespondenciaEntrada, DocumentManager

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'asunto', 'fecha_recepcion', 'remitente', 'destinatario', 'estado')
    search_fields = ('numero_documento','asunto','remitente','destinatario')
    list_filter  = ('estado','departamento_destino')

@admin.register(DocumentManager)
class DocumentManagerAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','telefono')
    search_fields = ('nombre','email')
