from django.contrib import admin
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_recepcion', 'remitente')

class CorrespondenciaSalidaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_envio', 'destinatario')

class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo')  # 'departamento' ha sido eliminado

admin.site.register(CorrespondenciaEntrada, CorrespondenciaEntradaAdmin)
admin.site.register(CorrespondenciaSalida, CorrespondenciaSalidaAdmin)
admin.site.register(Gestor, GestorAdmin)
