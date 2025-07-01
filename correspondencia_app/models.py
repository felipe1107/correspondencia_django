from django.db import models
from django.utils import timezone

class DocumentManager(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Gestor'
        verbose_name_plural = 'Gestores'
        ordering = ['nombre']  # Ahora siempre ordena alfabéticamente

class CorrespondenciaEntrada(models.Model):
    numero_documento = models.PositiveIntegerField(unique=True)
    asunto = models.CharField(max_length=200)
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    gestor = models.ForeignKey(
        DocumentManager,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    archivo_adjunto = models.FileField(
        upload_to='entradas/',
        null=True,
        blank=True
    )
    estado = models.CharField(
        max_length=20,
        choices=(
            ('Pendiente', 'Pendiente'),
            ('Recibido', 'Recibido'),
            ('Enviado', 'Enviado'),
        ),
        default='Pendiente'
    )
    fecha_recepcion = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Si no tiene número, le asignamos el siguiente
        if not self.numero_documento:
            último = CorrespondenciaEntrada.objects.aggregate(
                models.Max('numero_documento')
            )['numero_documento__max'] or 0
            self.numero_documento = último + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.numero_documento} – {self.asunto}"

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-fecha_recepcion']  # Las más recientes primero
