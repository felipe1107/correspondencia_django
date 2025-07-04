from django.contrib import admin
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = (
        'numero_documento', 'fecha_recepcion', 'remitente',
        'destinatario', 'asunto', 'departamento_destino', 'estado'
    )
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')
    list_filter = ('departamento_destino', 'estado', 'fecha_recepcion')
    date_hierarchy = 'fecha_recepcion'

@admin.register(CorrespondenciaSalida)
class CorrespondenciaSalidaAdmin(admin.ModelAdmin):
    list_display = (
        'numero_documento',
        # 'fecha_envio',  # ❌ Comentado si no existe
        'destinatario', 'asunto',
        'departamento_origen', 'estado'
    )
    search_fields = ('numero_documento', 'remitente', 'destinatario', 'asunto')
    list_filter = ('departamento_origen', 'estado')
    # date_hierarchy = 'fecha_envio'

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')  # ✅ Usamos campos que sí existen
    search_fields = ('nombre', 'correo')
