# correspondencia_app/models.py

from django.db import models

class CorrespondenciaEntrada(models.Model):
    ESTADOS = [
        ('RECIBIDO', 'Recibido'),
        ('ENVIADO', 'Enviado'),
    ]

    numero_documento      = models.CharField(max_length=100)
    remitente             = models.CharField(max_length=100)
    destinatario          = models.CharField(max_length=100)
    departamento_destino  = models.CharField(max_length=100)
    fecha_recepcion       = models.DateField()
    asunto                = models.CharField(max_length=200)
    observaciones         = models.TextField(blank=True)
    estado                = models.CharField(max_length=20, choices=ESTADOS)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return f"{self.numero_documento} – {self.remitente}"


class DocumentManager(models.Model):
    nombre   = models.CharField(max_length=100, blank=True)
    email    = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Gestor de Documentos"
        verbose_name_plural = "Gestores de Documentos"

    def __str__(self):
        return self.nombre or "(sin nombre)"
