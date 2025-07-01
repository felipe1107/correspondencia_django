from django.db import models
from django.utils import timezone

class DocumentManager(models.Model):
    nombre    = models.CharField(max_length=100)
    email     = models.EmailField(max_length=100, unique=True)
    telefono  = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre

class CorrespondenciaEntrada(models.Model):
    numero_documento = models.CharField(
        max_length=10,
        unique=True,
        editable=False,
        help_text="Número secuencial autogenerado, p.ej. 0001, 0002…"
    )
    asunto           = models.CharField(max_length=200)
    remitente        = models.CharField(max_length=100, blank=True)
    destinatario     = models.CharField(max_length=100, blank=True)
    fecha_recepcion  = models.DateField(
        default=timezone.now,
        editable=False,
        help_text="Se asigna la fecha de hoy al crear"
    )
    estado           = models.CharField(
        max_length=50,
        choices=[
            ('Recibido', 'Recibido'),
            ('En Proceso', 'En Proceso'),
            ('Finalizado', 'Finalizado'),
        ],
        default='Recibido'
    )
    gestor           = models.ForeignKey(
        DocumentManager,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    archivo_adjunto  = models.FileField(
        upload_to='entradas/',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        """Al primer guardado genera numero_documento y usa fecha por defecto."""
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            # Asigna un número secuencial con 4 dígitos según su PK
            self.numero_documento = str(self.pk).zfill(4)
            super().save(update_fields=['numero_documento'])

    def __str__(self):
        return f"{self.numero_documento} – {self.asunto}"
