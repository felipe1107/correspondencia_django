from django.contrib import admin
from .models import CorrespondenciaEntrada, DocumentManager

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = (
        'numero_documento',
        'asunto',
        'remitente',
        'destinatario',
        'gestor',
        'fecha_recepcion',
    )
    list_filter = (
        'gestor',
        'fecha_recepcion',
    )
    search_fields = ('numero_documento', 'asunto', 'remitente', 'destinatario')
    ordering = ('-fecha_recepcion',)

@admin.register(DocumentManager)
class DocumentManagerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')
    ordering = ('nombre',)
