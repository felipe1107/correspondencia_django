from django.db import models
from django.utils import timezone

class DocumentManager(models.Model):
    nombre    = models.CharField("Nombre", max_length=100)
    email     = models.EmailField("Email")
    telefono  = models.CharField("Teléfono", max_length=20)
    archivo   = models.FileField("Archivo", upload_to='gestores/', blank=True, null=True)

    class Meta:
        verbose_name        = "Gestor de Documentos"
        verbose_name_plural = "Gestores de Documentos"
        ordering            = ['nombre']

    def __str__(self):
        return self.nombre


class CorrespondenciaEntrada(models.Model):
    numero_documento     = models.CharField(
        "Número de documento",
        max_length=10,
        unique=True,
        editable=False  # no se edita a mano
    )
    fecha_recepcion      = models.DateField(
        "Fecha de recepción",
        auto_now_add=True  # se fija al crear
    )
    remitente            = models.CharField("Remitente", max_length=100)
    destinatario         = models.CharField("Destinatario", max_length=100)
    asunto               = models.CharField("Asunto", max_length=200)
    departamento_destino = models.CharField("Departamento destino", max_length=100)
    estado               = models.CharField("Estado", max_length=50)
    gestor               = models.ForeignKey(
        DocumentManager,
        verbose_name="Gestor responsable",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='entradas'
    )
    archivo_adjunto      = models.FileField(
        "Archivo adjunto",
        upload_to='entradas/',
        blank=True,
        null=True
    )
    observaciones        = models.TextField("Observaciones", blank=True)

    class Meta:
        verbose_name        = "Entrada de Correspondencia"
        verbose_name_plural = "Entradas de Correspondencia"
        ordering            = ['-fecha_recepcion']

    def __str__(self):
        return f"{self.numero_documento} — {self.asunto}"

    def save(self, *args, **kwargs):
        # Primero guardamos para obtener un PK
        if not self.pk:
            super().save(*args, **kwargs)
            # Genera el número secuencial con ceros a la izquierda (4 dígitos)
            self.numero_documento = f"{self.pk:04d}"
            # Ahora guarda de nuevo con el número asignado
            return super().save(*args, **kwargs)
        else:
            return super().save(*args, **kwargs)
