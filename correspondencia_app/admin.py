# correspondencia_app/admin.py

from django.contrib import admin
from .models import CorrespondenciaEntrada, DocumentManager

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'remitente', 'destinatario', 'fecha_recepcion', 'estado')
    search_fields = ('numero_documento', 'remitente', 'destinatario')

@admin.register(DocumentManager)
class DocumentManagerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')
