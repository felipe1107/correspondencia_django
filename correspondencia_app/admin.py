from django.contrib import admin
from .models import CorrespondenciaEntrada, Gestor

@admin.register(CorrespondenciaEntrada)
class CorrespondenciaEntradaAdmin(admin.ModelAdmin):
    list_display = (
        "numero_documento",
        "asunto",
        "gestor",
        "fecha_recepcion",
        "archivo_adjunto",
    )
    search_fields = ("asunto", "gestor__nombre")
    list_filter = ("gestor", "fecha_recepcion")
    readonly_fields = ("numero_documento", "fecha_recepcion")

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
