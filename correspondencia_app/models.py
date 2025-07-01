from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Gestor(models.Model):
    nombre = models.CharField(max_length=100)
    # ... demás campos de Gestor ...

    def __str__(self):
        return self.nombre


class CorrespondenciaEntrada(models.Model):
    numero_documento = models.IntegerField(
        unique=True,
        editable=False,
        verbose_name="Número de entrada"
    )
    asunto = models.CharField(max_length=200)
    gestor = models.ForeignKey(
        Gestor,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="entradas"
    )
    fecha_recepcion = models.DateField(
        default=timezone.now,
        editable=False,
        verbose_name="Fecha de recepción"
    )
    archivo_adjunto = models.FileField(
        upload_to="entradas/",
        null=True,
        blank=True
    )
    # ... cualquier otro campo que tengas ...

    def save(self, *args, **kwargs):
        # Si aún no tiene número, calculamos el siguiente
        if not self.numero_documento:
            ultimo = (
                CorrespondenciaEntrada.objects
                .aggregate(models.Max("numero_documento"))
                .get("numero_documento__max") or 0
            )
            self.numero_documento = ultimo + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.numero_documento} – {self.asunto}"
