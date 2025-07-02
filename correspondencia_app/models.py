from django.db import models
from django.utils import timezone

# Modelo de gestor de correspondencia
class Gestor(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    correo = models.EmailField("Correo electrónico", blank=True)

    def __str__(self):
        return self.nombre

# Modelo de correspondencia entrante
class CorrespondenciaEntrada(models.Model):
    numero_documento = models.PositiveIntegerField("Número", unique=True)
    asunto = models.CharField("Asunto", max_length=200)
    gestor = models.ForeignKey(
        Gestor,
        verbose_name="Gestor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    fecha_recepcion = models.DateField("Fecha de recepción", default=timezone.now)
    archivo_adjunto = models.FileField(
        "Archivo adjunto", upload_to='entradas/', blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            ultimo = type(self).objects.order_by('-numero_documento').first()
            self.numero_documento = (ultimo.numero_documento + 1) if ultimo else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.numero_documento} – {self.asunto}"

# Modelo de correspondencia saliente
class CorrespondenciaSalida(models.Model):
    numero_documento = models.CharField("Número de documento", max_length=20)
    fecha_envio = models.DateField("Fecha de envío")
    remitente = models.CharField("Remitente", max_length=100)
    destinatario = models.CharField("Destinatario", max_length=100)
    asunto = models.TextField("Asunto")
    departamento_origen = models.CharField("Departamento de origen", max_length=100)
    estado = models.CharField("Estado", max_length=50)
    archivo_adjunto = models.FileField("Archivo adjunto", upload_to='salidas/', blank=True, null=True)
    observaciones = models.TextField("Observaciones", blank=True, null=True)

    def __str__(self):
        return f"{self.numero_documento} - {self.asunto}"
