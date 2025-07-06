from django.contrib import admin
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor, Usuario

class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_recepcion', 'remitente', 'destinatario', 'asunto', 'departamento_destino', 'estado')

class CorrespondenciaSalidaAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'fecha_envio', 'remitente', 'destinatario', 'asunto', 'departamento_origen', 'estado')

class GestorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'correo')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'rol')

admin.site.register(CorrespondenciaEntrada, CorrespondenciaEntradaAdmin)
admin.site.register(CorrespondenciaSalida, CorrespondenciaSalidaAdmin)
admin.site.register(Gestor, GestorAdmin)
admin.site.register(Usuario, UsuarioAdmin)
